from typing import Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Gold',
        '155',
        'Silver',
        '10',
        'Copper',
        '17',
        'stop',
    ),
    (
        'gold',
        '155',
        'silver',
        '10',
        'copper',
        '17',
        'gold',
        '15',
        'stop',
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
        self.resources: Dict = dict()

    def run(self) -> None:
        while True:
            line_in: str = input()
            if line_in == 'stop':
                break
            elif line_in in self.resources:
                self.resources[line_in] += int(input())
            else:
                self.resources[line_in] = int(input())
        for k, v in self.resources.items():
            print(f"{k} -> {v}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
