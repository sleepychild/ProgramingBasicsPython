import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "The waterfall was so high, that the child could't see its peak.",
        "the",
    ),
    (
        "How do you plan on achieving that? How? How can you even think of that?",
        "how",
    ),
    (
        "There was one. Therefore I bought it. I wouldn't buy it otherwise.",
        "there",
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
        self.ss: str = input()
        self.re: str = fr"(?P<generic>\b{self.ss}\b)\b"
        self.rg: str = 'generic'

    def run(self) -> None:
        rr: List[str] = list()
        if DEBUG:
            print(self.re)
            print(self.ts)
        for r in re.finditer(self.re, self.ts, re.IGNORECASE):
            rr.append(r.group(self.rg))                
        print(len(rr))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
