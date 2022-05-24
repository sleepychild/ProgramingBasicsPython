from typing import List, Tuple, Generator, Callable, Union
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "2",
        "Peter",
        "Amy",
        "Start",
        "2",
        "refill 1",
        "1",
        "End",
    ),
    (
        "10",
        "Peter",
        "George",
        "Amy",
        "Alice",
        "Start",
        "2",
        "3",
        "3",
        "3",
        "End",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    water: int = int(input())
    que: deque = deque()
    while True:
        lin: str = input()
        if lin == "Start":
            break
        else:
            que.append(lin)
    while True:
        lin: List[str] = input().split()
        if lin[0] == "refill":
            water += int(lin[1])
        elif lin[0] == "End":
            print(f"{water} liters left")
            break
        else:
            water_wanted: int = int(lin[0])
            if water_wanted <= water:
                print(f"{que.popleft()} got water")
                water -= water_wanted
            else:
                print(f"{que.popleft()} must wait")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
