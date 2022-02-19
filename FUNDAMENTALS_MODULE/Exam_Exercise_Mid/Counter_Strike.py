from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '100',
        '10',
        '10',
        '10',
        '1',
        '2',
        '3',
        '73',
        '10',
    ),
    (
        '200',
        '54',
        '14',
        '28',
        '13',
        'End of battle',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


FIRST: int = 0
LAST: int = -1


class Directions(Enum):
    UP: Tuple[int] = (-1, 0,)
    RIGHT: Tuple[int] = (0, 1,)
    DOWN: Tuple[int] = (1, 0,)
    LEFT: Tuple[int] = (0, -1,)


class Base:

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:
    def __init__(self) -> None:
        self.nrj: int = int(input())
        self.bw: int = int()

    def run(self) -> None:
        while True:
            cmd: str = input()
            if cmd == 'End of battle':
                print(f'Won battles: {self.bw}. Energy left: {self.nrj}')
                break
            else:
                distance: int = int(cmd)
                if self.nrj >= distance:
                    self.nrj -= distance
                    self.bw += 1
                    if self.bw % 3 == 0:
                        self.nrj += self.bw
                else:
                    print(f'Not enough energy! Game ends with {self.bw} won battles and {self.nrj} energy')
                    break


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
