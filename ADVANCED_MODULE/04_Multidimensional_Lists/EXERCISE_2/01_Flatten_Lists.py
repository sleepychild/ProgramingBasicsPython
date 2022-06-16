from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("1 2 3 |4 5 6 | 7 88",),
    ("7 | 4 5|1 0| 2 5 |3",),
    ("1| 4 5 6 7 | 8 9",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    sub_matrixes: List[List[str]] = list()
    for sub_matrix in [sm.split() for sm in input().split("|")[::-1]]:
        sub_matrixes.extend(sub_matrix)
    print(" ".join(sub_matrixes))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
