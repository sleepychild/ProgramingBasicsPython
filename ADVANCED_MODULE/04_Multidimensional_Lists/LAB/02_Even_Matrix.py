from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "2",
        "1, 2, 3",
        "4, 5, 6",
    ),
    (
        "4",
        "10, 33, 24, 5, 1",
        "67, 34, 11, 110, 3",
        "4, 12, 33, 63, 21",
        "557, 45, 23, 55, 67",
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
        matrix.append(list(filter(lambda x: x % 2 == 0, map(int, input().split(", ")))))

    print(matrix)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
