from typing import List, Tuple, Generator, Callable, Union
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "George",
        "Peter",
        "William",
        "Paid",
        "Michael",
        "Oscar",
        "Olivia",
        "Linda",
        "End",
    ),
    (
        "Anna",
        "Emma",
        "Alexander",
        "End",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    que = deque()
    while True:
        lin: str = input()
        if lin == "Paid":
            while que:
                print(que.popleft())
        elif lin == "End":
            print(f"{len(que)} people remaining.")
            break
        else:
            que.append(lin)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
