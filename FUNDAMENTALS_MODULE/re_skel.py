import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = True

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '',
    ),
    (
        '',
    ),
    (
        '',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.re: str = r"(?P<generic>.*)\b"
        self.rg: str = 'generic'

    def run(self) -> None:
        rr: List[str] = list()
        while True:
            try:
                lin: str = input()
                if lin == '':
                    break
                for r in re.finditer(self.re, lin):
                    rr.append(r.group(self.rg))
            except (StopIteration, EOFError,) as _:
                break
        print(''.join(rr))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
