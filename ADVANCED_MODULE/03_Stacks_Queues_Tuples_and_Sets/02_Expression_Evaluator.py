from collections import deque
from typing import Generator, Callable, Tuple, Deque
from math import floor
from functools import reduce

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("6 3 - 2 1 * 5 /",),
    ("2 2 - 1 *",),
    ("10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    numbers: Deque[int] = deque()
    for element in input().split():
        if not element in "*+-/":
            numbers.append(int(element))
        else:
            if DEBUG:
                print(
                    f"{element.join(map(str, numbers))} =",
                    reduce(lambda x, y: eval(f"{x}{element}{y}"), numbers),
                )
            ev_res: float = reduce(lambda x, y: eval(f"{x}{element}{y}"), numbers)
            numbers.clear()
            numbers.append(floor(ev_res))
            # ev_res: float = float(numbers.popleft())
            # while numbers:
            #     ev_res = eval(f"{ev_res} {element} {numbers.popleft()}")
            # numbers.append(floor(ev_res))
    print(numbers[0])


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
