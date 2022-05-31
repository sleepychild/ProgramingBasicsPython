from typing import Deque, Tuple, Generator, Callable
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5 4 8 6 3 8 7 7 9",
        "16",
    ),
    (
        "1 7 8 2 5 4 7 8 9 6 3 2 5 4 6",
        "20",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    clothes: Deque = deque([int(c) for c in input().split()])
    rack_capacity: int = int(input())
    racks_count: int = int()

    while clothes:
        acc: int = int()
        while acc <= rack_capacity:
            if clothes and acc + clothes[-1] <= rack_capacity:
                acc += clothes.pop()
            else:
                racks_count += 1
                break

    print(racks_count)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
