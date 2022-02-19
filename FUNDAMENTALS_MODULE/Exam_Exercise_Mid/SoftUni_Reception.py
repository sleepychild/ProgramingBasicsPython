from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        '6',
        '4',
        '20',
    ),
    (
        '1',
        '2',
        '3',
        '45',
    ),
    (
        '3',
        '2',
        '5',
        '40',
    ),
    (
        '1',
        '1',
        '1',
        '7',
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
        self.r_a: int = int(input())
        self.r_b: int = int(input())
        self.r_c: int = int(input())
        self.sq: int = int(input())
        self.tn: int = int()

    def tick(self) -> None:
        self.tn += 1
        if self.tn % 4 != 0:
            self.sq -= self.r_a
            self.sq -= self.r_b
            self.sq -= self.r_c

    def run(self) -> None:
        while self.sq > 0:
            self.tick()

        print(f'Time needed: {self.tn}h.')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
