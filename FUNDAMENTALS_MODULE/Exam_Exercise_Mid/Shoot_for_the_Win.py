from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '24 50 36 70',
        '0',
        '4',
        '3',
        '1',
        'End',
    ),
    (
        '30 30 12 60 54 66',
        '5',
        '2',
        '4',
        '0',
        'End',
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
        self.targets: List[int] = [ int(i) for i in input().split(' ') ]

    def run(self) -> None:
        count: int = int()
        while True:
            cmd: str = input()
            if cmd == 'End':
                print(f"Shot targets: {count} -> {' '.join([ str(i) for i in self.targets ])}")
                break
            else:
                hit: int = int(cmd)
                if hit in range(len(self.targets)):
                    hit_val: int = self.targets[hit]
                    if hit_val != -1:
                        count += 1
                        self.targets[hit] = -1
                        for k,v in enumerate(self.targets):
                            if v != -1:
                                if v > hit_val:
                                    self.targets[k] -= hit_val
                                else:
                                    self.targets[k] += hit_val


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
