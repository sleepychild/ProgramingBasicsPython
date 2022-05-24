from typing import List, Tuple, Generator, Callable, Union
from string import digits, ascii_letters

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5",),
    ("(2 + 3) - (2 + 3)",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input

def solution():
    lin: List = list(input())
    depth_stack: List[int] = list()

    for i,e in enumerate(lin):
        if e == "(":
            depth_stack.append(i)
        elif e == ")":
            print("".join(lin[depth_stack.pop():i+1]))

if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
