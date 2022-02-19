from math import ceil
from typing import List, Tuple, Generator, Callable
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        '25',
        '30',
        '12',
        '19',
        '24',
        '16',
        '20',
    ),
    (
        '10',
        '30',
        '14',
        '8',
        '23',
        '27',
        '28',
        '15',
        '17',
        '25',
        '26',
        '5',
        '18',
    ),
    (
        '0',
        '0',
        '0',
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

    def __init__(self, attendaces: List[int], lectures_count: int, bonus: int) -> None:
        self.att: List[int] = attendaces
        self.lec: int = lectures_count
        self.bns: int = bonus

    def formula(self, a) -> int:
        try:
            return ceil(( a / self.lec ) * ( 5 + self.bns ))
        except ZeroDivisionError as _:
            return 0

    def __str__(self) -> str:
        return_str: str = str()
        for a in self.att:
            return_str += f'{a} : {self.formula(a)}\n'
        return return_str            

    @classmethod
    def FromInput(cls) -> 'Base':
        student_count: int = int(input())
        lectures_count: int = int(input())
        bonus: int = int(input())
        attendaces: List[int] = list()
        for _ in range(student_count):
            attendaces.append(int(input()))
        return cls(attendaces, lectures_count, bonus)


class ControlClass:

    def __init__(self) -> None:
        self.data: Base = Base.FromInput() 

    def run(self) -> None:
        if DEBUG: print(self.data)
        try:
            max_att: int = max(self.data.att)
        except ValueError as _:
            max_att: int = 0
        print(f'Max Bonus: {self.data.formula(max_att)}.\nThe student has attended {max_att} lectures.')

def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
