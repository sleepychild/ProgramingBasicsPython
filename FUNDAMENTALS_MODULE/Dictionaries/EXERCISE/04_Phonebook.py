from typing import Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Adam-0888080808',
        '2',
        'Mery',
        'Adam',
    ),
    (
        'Adam-+359888001122',
        'Ralf-666',
        'George-5559393',
        'Silvester-02/987665544',
        '4',
        'Silvester',
        'silvester',
        'Rolf',
        'Ralf',
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

    def run(self) -> None:
        phonebook: Dict = dict()
        while True:
            line_in: str = input()
            if line_in.find('-') == -1:
                break
            else:
                name, num = line_in.split('-')
                phonebook.update({name: num})
        for _ in range(int(line_in)):
            query: str = input()
            try:
                print(f'{query} -> {phonebook[query]}')
            except KeyError as e:
                print(f'Contact {query} does not exist.')



def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
