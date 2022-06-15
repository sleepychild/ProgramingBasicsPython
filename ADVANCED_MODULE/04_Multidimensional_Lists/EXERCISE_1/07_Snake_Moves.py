from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5 6",
        "SoftUni",
    ),
    (
        "1 4",
        "Python",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def chr_feed(line_in: str) -> Generator[str, None, None]:
    while True:
        for c in line_in:
            yield c


def solution() -> None:
    rows: int
    cols: int

    rows, cols = map(int, input().split())

    cf: Generator[str, None, None] = chr_feed(input())

    matrix: List[List[str]] = list(
        [list(["" for _ in range(cols)]) for _ in range(rows)]
    )

    for row in range(rows):
        for col in range(cols) if (row % 2 == 0) else range(cols - 1, -1, -1):
            if DEBUG:
                print(row, col)
            matrix[row][col] = next(cf)

    for row in matrix:
        print("".join(map(str, row)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
