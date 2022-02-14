from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '3',
        '1 0 0 1',
        '2 0 0 0',
        '0 3 0 1',
        '0-0 1-0 2-1 2-1 2-1 1-1 2-1',
    ),
    (
        '5',
        '1 0 5 0 1',
        '6 3 9 0 0',
        '7 9 4 3 2',
        '1 0 0 4 9',
        '5 6 0 3 5',
        '0-1 0-2 0-2 0-2 0-2 0-2 3-0',
    ),    
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)
    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

class GridClass:
    
    def __init__(self, grid: List[List[int]]) -> None:
        self.grid: List[List[int]] = grid
        self.ship_count: int = int(self)

    def attack(self) -> None:
        for r, c in [ [ int(at) for at in atk.split('-') ] for atk in input().split(' ') ]:
            try:
                self.grid[r][c] -= 1
            except IndexError as _:
                pass
            if DEBUG: print(f'{r} - {c}\n{self}')

    def __str__(self) -> str:
        string_out: str = str()
        for row in self.grid:
            string_out += f"{' '.join([str(e) for e in row])}\n"
        return string_out

    def __int__(self) -> int:
        count: int = int()
        for row in self.grid:
            for col in row:
                count += 1 if col > 0 else 0
        return count

    @staticmethod
    def row_from_string(row_string: str) -> List[int]:
        return [ int(l) for l in row_string.split(' ')]

    @classmethod
    def FromInput(cls) -> 'GridClass':
        grid: List[List[int]] = list()
        for i in range(int(input())):
            grid.append(cls.row_from_string(input()))
        return cls(grid)

def solution():
    grid: GridClass = GridClass.FromInput()
    if DEBUG: print(grid)
    grid.attack()
    print(grid.ship_count - int(grid))

if DEBUG: 
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
