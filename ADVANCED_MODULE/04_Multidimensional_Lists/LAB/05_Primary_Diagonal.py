from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "11 2 4",
        "4 5 6",
        "10 8 -12",
    ),
    (
        "3",
        "1 2 3",
        "4 5 6",
        "7 8 9",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    diagonal: int = int(input())
    diagonal_sum: int = int()
    matrix: List[List[int]] = list()

    for _ in range(diagonal):
        matrix.append(list(map(int, input().split())))

    for i in range(diagonal):
        diagonal_sum += matrix[i][i]

    print(diagonal_sum)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
