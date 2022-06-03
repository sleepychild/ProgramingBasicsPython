from collections import deque
from typing import Deque, Generator, Callable, List, Tuple


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4 2 10 5",
        "3 15 15 11 6",
    ),
    (
        "1 5 28 1 4",
        "3 18 1 9 30 4 5",
    ),
    (
        "10 20 30 40 50",
        "20 11",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    cups: Deque[int] = deque([int(c) for c in input().split()])
    btls: Deque[int] = deque([int(b) for b in input().split()])

    if DEBUG:
        print(cups)
        print(btls)

    waste: int = int()

    while cups and btls:
        cup: int = cups.popleft()

        while cup > 0:
            cup -= btls.pop()

        waste += abs(cup)

    if DEBUG:
        print(cups)
        print(btls)
        print(waste)

    if cups:
        print(f"Cups: {' '.join([str(c) for c in cups])}")

    if btls:
        print(f"Bottles: {' '.join([str(b) for b in btls])}")

    print(f"Wasted litters of water: {waste}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
