from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "2",
        "1, 2, 3",
        "4, 5, 6",
    ),
    (
        "3",
        "10, 2, 21, 4",
        "5, 20, 41, 9",
        "6, 2, 4, 99",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    matrix: List[List[int]] = list()

    for _ in range(int(input())):
        matrix.extend(map(int, input().split(", ")))

    print(matrix)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
