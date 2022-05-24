from typing import List, Tuple, Generator, Callable, Union, Deque
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "Tracy Emily Daniel",
        "2",
    ),
    (
        "George Peter Michael William Thomas",
        "10",
    ),
    (
        "George Peter Michael William Thomas",
        "1",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    players: Deque[str] = deque(input().split())
    hops: int = int(input())
    while len(players) > 1:
        players.rotate(-hops)
        print(f"Removed {players.pop()}")
    print(f"Last is {players.pop()}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
