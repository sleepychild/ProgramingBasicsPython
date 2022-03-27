import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "Please contact us at: support@github.com.",
    ),
    (
        "Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.",
    ),
    (
        "Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.ts: str = input()
        self.rg: str = "generic"
        self.re: str = fr"\s(?P<generic>(?P<user>[A-Za-z][A-Za-z0-9._-]+)@(?P<host>\w+([.-]\w+)+))\b"

    def run(self) -> None:
        rr: List[str] = list()
        if DEBUG:
            print(self.re)
            print(self.ts)
        for r in re.finditer(self.re, self.ts, re.IGNORECASE):
            print(r.group(self.rg))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
