import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'The _id and _age variables are both integers.',
    ),
    (
        'Calculate the _area of the _perfectRectangle object.',
    ),
    (
        '__invalidVariable _evenMoreInvalidVariable_ _validVariable',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.re: str = r"\b_(?P<variable>[A-Za-z0-9]+)\b"

    def run(self) -> None:
        rr: List[str] = list()
        while True:
            try:
                lin: str = input()
                if lin == '':
                    break
                for r in re.finditer(self.re, lin):
                    rr.append(r.group('variable'))
            except (StopIteration, EOFError,) as _:
                break
        print(','.join(rr))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
