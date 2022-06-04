from collections import deque
from typing import Deque, Generator, Callable, List, Tuple


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3",),
    ("2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    numbers_list: List[str] = [float(n) for n in input().split(" ")]

    while numbers_list:
        num: float = numbers_list[0]
        print(f"{num:.1f} - {numbers_list.count(num)} times")
        while num in numbers_list:
            numbers_list.remove(num)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
