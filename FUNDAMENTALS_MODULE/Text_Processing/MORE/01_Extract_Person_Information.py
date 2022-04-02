
from typing import List, Tuple, Generator, Callable, Union
from enum import Enum
import re

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '2',
        'Here is a name @George| and an age #18*',
        'Another name @Billy| #35* is his age',
    ),
    (
        '3',
        'random name @lilly| random digits #5*age',
        '@Marry| with age #19*',
        'here Comes @Garry|he is #48* years old',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def run(self) -> None:
        for _ in range(int(input())):
            lin: str = input()
            name = re.search(r'@(?P<name>.+)\|', lin)
            age = re.search(r'#(?P<age>\d+)\*', lin)
            if name and age:
                print(f"{name.group('name')} is {age.group('age')} years old.")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
