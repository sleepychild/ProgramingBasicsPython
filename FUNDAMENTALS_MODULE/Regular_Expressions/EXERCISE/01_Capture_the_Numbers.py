import re
from typing import List, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "The300",
        "What is that?",
        "I think it's the 3rd movie",
        "Let's watch it at 22:45",
    ),
    (
        "123a456",
        "789b987",
        "654c321",
        "0",
    ),
    (
        "Let's go11!!!11!",
        "Okey!1!",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.re: str = r"(?P<number>\d+)"


    def run(self) -> None:
        while True:
            try:
                lin: str = input()
                if lin == '':
                    break
                for r in re.finditer(self.re, lin):
                    print(r.group('number'), end=' ')
            except StopIteration as _:
                break


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
