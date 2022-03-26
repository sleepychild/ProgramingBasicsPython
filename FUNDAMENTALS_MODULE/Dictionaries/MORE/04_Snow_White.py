from typing import Dict, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Peter <:> Red <:> 2000',
        'Teodor <:> Blue <:> 1000',
        'George <:> Green <:> 1000',
        'Simon <:> Yellow <:> 4500',
        'Dopey <:> Simon <:> 1000',
        'Once upon a time',
    ),
    (
        'Grumpy <:> Red <:> 5000',
        'Grumpy <:> Blue <:> 10000',
        'Grumpy <:> Red <:> 10000',
        'Happy <:> Blue <:> 10000',
        'Once upon a time',
    ),
    (
        'A <:> A <:> 10000',
        'B <:> B <:> 10000',
        'C <:> C <:> 10000',
        'D <:> D <:> 10000',
        'A <:> D <:> 10000',
        'Once upon a time',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.dwarfs: Dict[str, Dict[str, Union[str, int]]] = dict()
        self.colors: Dict[str, int] = dict()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'Once upon a time':
                break
            name, color, physics = lin.split(' <:> ')
            dk = f"{color}_{name}"
            physics = int(physics)
            if dk not in self.dwarfs:
                if color in self.colors:
                    self.colors[color] += 1
                else:
                    self.colors[color] = 1
                dwrf: Dict[str, Union[str, int]] = {
                    "name": name,
                    "color": color,
                    "physics": physics
                }
                self.dwarfs[dk] = dwrf
            else:
                self.dwarfs[dk]["physics"] = max(physics, self.dwarfs[dk]["physics"])

        if DEBUG:
            print(self.colors)
            print(self.dwarfs)
        self.dwarfs: Dict[str, Dict[str, Union[str, int]]] = dict(sorted(self.dwarfs.items(), key=lambda i: self.colors[i[1]["color"]], reverse=True))
        if DEBUG: print(self.dwarfs)
        self.dwarfs: Dict[str, Dict[str, Union[str, int]]] = dict(sorted(self.dwarfs.items(), key=lambda i: i[1]["physics"], reverse=True))

        for d in self.dwarfs.values():
            print(f'({d["color"]}) {d["name"]} <-> {d["physics"]}')

def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
