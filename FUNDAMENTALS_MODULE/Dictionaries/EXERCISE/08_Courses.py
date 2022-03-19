from typing import Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Programming Fundamentals : John Smith',
        'Programming Fundamentals : Linda Johnson',
        'JS Core : Will Wilson',
        'Java Advanced : Harrison White',
        'end',
    ),
    (
        'Algorithms : Jay Moore',
        'Programming Basics : Martin Taylor',
        'Python Fundamentals : John Anderson',
        'Python Fundamentals : Andrew Robinson',
        'Algorithms : Bob Jackson',
        'Python Fundamentals : Clark Lewis',
        'end',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.courses: Dict[str, List[str]] = dict()

    def run(self) -> None:
        while True:
            li: str = input()
            if li == 'end':
                break

            c, s = li.split(" : ")
            if c not in self.courses:
                self.courses[c] = list()

            self.courses[c].append(s)

        for k, v in self.courses.items():
            print(f"{k}: {len(v)}")
            for s in v:
                print(f"-- {s}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
