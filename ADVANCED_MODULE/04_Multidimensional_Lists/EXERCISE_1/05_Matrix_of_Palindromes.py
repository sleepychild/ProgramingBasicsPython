from typing import Generator, Callable, Tuple, List
from string import ascii_lowercase

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("4 6",),
    ("3 2",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    rows: int
    cols: int
    rows, cols = map(int, input().split())

    for row in range(rows):
        for col in range(cols):
            print(
                f"{ascii_lowercase[row]}{ascii_lowercase[row+col]}{ascii_lowercase[row]}",
                end=" ",
            )
        print()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
