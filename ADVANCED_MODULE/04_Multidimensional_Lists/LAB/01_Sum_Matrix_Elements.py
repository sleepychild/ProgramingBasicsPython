from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3, 6",
        "7, 1, 3, 3, 2, 1",
        "1, 3, 9, 8, 5, 6",
        "4, 6, 7, 9, 1, 0",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    rows: int
    rows, _ = map(int, input().split(", "))

    matrix: List[List[int]] = list()

    for _ in range(rows):
        matrix.append(list(map(int, input().split(", "))))

    print(sum([sum(r) for r in matrix]))
    print(matrix)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
