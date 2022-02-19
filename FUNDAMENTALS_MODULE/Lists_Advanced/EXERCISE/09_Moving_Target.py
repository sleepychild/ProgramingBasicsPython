from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '52 74 23 44 96 110',
        'Shoot 5 10',
        'Shoot 1 80',
        'Strike 2 1',
        'Add 22 3',
        'End',
    ),
    (
        '47 55 85 78 99 20',
        'Shoot 1 55',
        'Shoot 8 15',
        'Strike 2 3',
        'Add 0 22',
        'Add 2 40',
        'Add 2 50',
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

class ShootingRangeClass:

    def __init__(self, targets: List[int]) -> None:
        self.targets: List[int] = targets

    def shoot(self, index: int, power: int) -> None:
        if self._validate_index(index):
            self.targets[index] -= power
            if DEBUG: print(f'Post Shoot: {self}')
            if self.targets[index] <= 0:
                _: int = self.targets.pop(index)
                if DEBUG: print(f'Post Clear: {self}')

    def add(self, index: int, value: int) -> None:
        if self._validate_index(index):
            self.targets.insert(index, value)
            if DEBUG: print(f'Post Add: {self}')
        else:
            print('Invalid placement!')

    def strike(self, index: int, radius: int) -> None:
        if self._validate_index(index) and self._validate_index(index-radius) and self._validate_index(index+radius):
            for _ in range(index-radius,index+radius+1):
                self.targets.pop(index-radius)
                if DEBUG: print(f'Post Strike: {self}')
        else:
            print('Strike missed!')

    def _validate_index(self, index: int) -> bool:
        return index in range(len(self.targets))

    def __str__(self) -> str:
        return '|'.join([str(n) for n in self.targets])

    @classmethod
    def FromInput(cls) -> 'ShootingRangeClass':
        return cls([ int(n) for n in input().split(' ') ])

class ControlClass:

    def __init__(self) -> None:
        self.sr: ShootingRangeClass = ShootingRangeClass.FromInput()

    def run(self) -> None:
        if DEBUG: print(f'\nSTART RUN: {self.sr}')

        while True:
            cmd: str = input()

            if cmd == 'End':
                print(self.sr)
                return

            c_act, c_ind, c_arg = [ int(p) if p.isnumeric() else p for p in cmd.split(' ') ]

            if DEBUG: print(c_act, c_ind, c_arg)
            
            if c_act == 'Shoot':
                self.sr.shoot(c_ind, c_arg)
            elif c_act == 'Add':
                self.sr.add(c_ind, c_arg)
            elif c_act == 'Strike':
                self.sr.strike(c_ind, c_arg)
            else:
                print(self.sr)
                return


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
