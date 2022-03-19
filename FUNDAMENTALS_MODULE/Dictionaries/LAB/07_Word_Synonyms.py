from typing import Tuple, Generator, Callable, Dict, List
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '3',
        'cute',
        'adorable',
        'cute',
        'charming',
        'smart',
        'clever',
    ),
    (
        '2',
        'task',
        'problem',
        'task',
        'assignment',
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
        self.word_count: int = int(input())
        self.synonym: Dict = dict()

    def run(self) -> None:
        for _ in range(self.word_count):
            word_in: str = input()
            syn_in: str = input()
            try:
                self.synonym[word_in].append(syn_in)
            except KeyError as e:
                self.synonym[word_in] = list()
                self.synonym[word_in].append(syn_in)

        for k, v in self.synonym.items():
            print(f"{k} - {', '.join(v)}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
