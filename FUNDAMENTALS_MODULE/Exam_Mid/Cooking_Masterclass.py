from typing import List, Tuple, Generator, Callable, Union
from enum import Enum
from math import ceil

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '50',
        '2',
        '1.0',
        '0.10',
        '10.0',
    ),
    (
        '100',
        '25',
        '4.0',
        '1.0',
        '6.0',
    ),
    (
        '946',
        '20',
        '12.05',
        '0.42',
        '27.89',
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

    def __init__(self) -> None:
        pass

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:

    def __init__(self) -> None:
        self.budget: float = float(input())
        self.students: int = int(input())
        self.flour_price: float = float(input())
        self.egg_price: float = float(input())
        self.apron_price: float = float(input())

    def run(self) -> None:
        aprons_needed: int = ceil(self.students * 1.2)
        aprons_expense: float = aprons_needed * self.apron_price

        egg_expese: float = (self.students * 10) * self.egg_price

        flour_needed: int = self.students - (self.students // 5)
        flour_expense: float = flour_needed * self.flour_price

        expenses: float = aprons_expense + egg_expese + flour_expense

        if self.budget >= expenses:
            print(f'Items purchased for {expenses:.2f}$.')
        else:
            print(f'{abs(self.budget - expenses):.2f}$ more needed.')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
