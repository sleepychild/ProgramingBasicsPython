from typing import Deque, Tuple, Generator, Callable
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "348",
        "20 54 30 16 7 9",
    ),
    (
        "499",
        "57 45 62 70 33 90 88 76 100 50",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    food_available: int = int(input())
    orders: Deque = deque([int(o) for o in input().split()])

    if DEBUG:
        print(food_available, orders)

    try:
        print(max(orders))
    except ValueError as _:
        pass

    while len(orders) > 0 and food_available >= orders[0]:
        food_available -= orders.popleft()
        if DEBUG:
            print(food_available, orders)

    if orders:
        print(f"Orders left: {' '.join([ str(o) for o in orders ])}")
    else:
        print("Orders complete")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
