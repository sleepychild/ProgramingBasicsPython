from typing import ClassVar, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '15',
        '0 0 0 0',
    ),
    (
        '20',
        '0 2 0',
    ),
    (
        '15',
        '0 0 0 0 0',
    ),
    (
        '12',
        '0 0 0',
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
    CAPACITY: ClassVar[int] = 4
    EMPTY: ClassVar[int] = 0

    def __init__(self) -> None:
        self.people_que: int = int(input())
        self.wagons: List[int] = [int(w) for w in input().split(' ')]

    def run(self) -> None:
        for k, v in enumerate(self.wagons):
            while v < self.CAPACITY and self.people_que > self.EMPTY:
                self.wagons[k] += 1
                self.people_que -= 1
                v += 1
        if len(list(filter(lambda w: w < self.CAPACITY, self.wagons))) > 0:
            print('The lift has empty spots!')
        elif self.people_que > self.EMPTY:
            print(
                f"There isn't enough space! {self.people_que} people in a queue!")
        print(' '.join([str(w) for w in self.wagons]))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
