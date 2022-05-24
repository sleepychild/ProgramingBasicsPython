from typing import Deque, Tuple, Generator, Callable
from collections import deque

DEBUG: bool = True

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4",
        "1 10",
        "1 20",
        "1 30",
        "1 40",
    ),
    (
        "9",
        "1 97",
        "2",
        "1 20",
        "2",
        "1 26",
        "1 20",
        "3",
        "1 91",
        "4",
    ),
    (
        "10",
        "2",
        "1 47",
        "1 66",
        "1 32",
        "4",
        "3",
        "1 25",
        "1 16",
        "1 8",
        "4",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    dq: Deque = deque()
    for _ in range(int(input())):
        lin: str = input()
        if lin.startswith("1 "):
            dq.append(int(lin[2:]))
        elif lin.startswith("2"):
            try:
                dq.pop()
            except IndexError as _:
                pass
        elif lin.startswith("3"):
            print(max(dq))
        elif lin.startswith("4"):
            print(min(dq))
    dq.reverse()
    print(", ".join(list(map(lambda e: str(e), dq))))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
