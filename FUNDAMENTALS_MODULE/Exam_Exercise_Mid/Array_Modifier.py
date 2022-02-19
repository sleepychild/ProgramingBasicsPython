from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '23 -2 321 87 42 90 -123',
        'swap 1 3',
        'swap 3 6',
        'swap 1 0',
        'multiply 1 2',
        'multiply 2 1',
        'decrease',
        'end',
    ),
    (
        '1 2 3 4',
        'swap 0 1',
        'swap 1 2',
        'swap 2 3',
        'multiply 1 2',
        'decrease',
        'end',
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
        self.nums: List[int] = [ int(i) for i in input().split(' ') ]

    def run(self) -> None:
        while True:
            cmd: str = input()
            if cmd == 'end':
                print(', '.join([ str(i) for i in self.nums ]))
                break
            elif cmd == 'decrease':
                for k,v in enumerate(self.nums):
                    self.nums[k] = v-1
            else:
                a, b, c = [ int(e) if e.isnumeric() else e for e in cmd.split(' ') ]
                if a == 'swap':
                    self.nums[b], self.nums[c] = self.nums[c], self.nums[b]
                elif a == 'multiply':
                    self.nums[b] = self.nums[b] * self.nums[c]



def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
