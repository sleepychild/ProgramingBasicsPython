from typing import Generator, List, Tuple, Callable

test_runs: Tuple[Tuple[str]] = (
    (
        '10@10@10@2',
        'Jump 1',
        'Jump 2',
        'Love!',
    ),
    (
        '2@4@2',
        'Jump 2',
        'Jump 2',
        'Jump 8',
        'Jump 3',
        'Jump 1',
        'Love!',
    ),
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)
    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

class HouseHasValentine(Exception):
    pass

class HouseHadValentine(Exception):
    pass

class HouseClass:

    def __init__(self, hearts_needed: int) -> None:
        self.hearts_needed: int = hearts_needed
        self.had_valentine: bool = False

    def visit(self, c_pow) -> None:
        if self.had_valentine:
            raise HouseHadValentine
        
        self.hearts_needed -= c_pow

        if self.hearts_needed == 0:
            self.had_valentine = True
            raise HouseHasValentine

    def __str__(self) -> str:
        return f'{self.hearts_needed} / {self.had_valentine}'

class NeighborhoodClass:

    def __init__(self, houses_list: List[int]) -> None:
        self.houses_list: List[HouseClass] = list()
        for house in houses_list:
            self.houses_list.append(HouseClass(house))
        self.house_count = len(self.houses_list)

    def visit(self, house: int, c_pow: int) -> int:
        try:
            self.houses_list[house].visit(c_pow)
        except IndexError as _:
            house = self.visit(0, c_pow)
        except HouseHasValentine as _:
            print(f"Place {house} has Valentine's day.")
        except HouseHadValentine as _:
            print(f"Place {house} already had Valentine's day.")
        finally:
            return house

    def result(self) -> None:
        print(f"Cupid has failed { len(list(filter(lambda h: not h.had_valentine, self.houses_list))) } places.")

    def __str__(self) -> str:
        return ' @ '.join(list(map(str,self.houses_list)))

    @classmethod
    def FromString(cls, houses_str: str) -> 'NeighborhoodClass':
        return cls([ int(x) for x in houses_str.split('@') ])

class CupidClass:

    def __init__(self, neighborhood: NeighborhoodClass) -> None:
        self.nbh: NeighborhoodClass = neighborhood
        self.position: int = int()
        self.power: int = 2
    
    def jump(self, jmp: int) -> None:
        self.position = self.nbh.visit(self.position + jmp, self.power)

    def run(self) -> None:
        while True:
            instruction: str = input()
            if instruction == 'Love!':
                break
            else:
                self.jump(int(instruction.split(' ')[1]))
        print(f"Cupid's last position was {self.position}.")
        self.nbh.result()

def solution():
    neighborhood: NeighborhoodClass = NeighborhoodClass.FromString(input())
    CupidClass(neighborhood).run()

solution()

# for test_run in test_runs:
#     input: Callable[[], str] = get_run_generator(test_run)
#     solution()
