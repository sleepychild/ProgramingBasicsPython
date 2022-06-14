from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4 5",
        "1 5 5 2 4",
        "2 1 4 14 3",
        "3 7 11 2 8",
        "4 8 12 16 4",
    ),
    (
        "5 6",
        "1 0 4 3 1 1",
        "1 3 1 3 0 4",
        "6 4 1 2 5 6",
        "2 2 1 5 4 1",
        "3 3 3 6 0 5",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


sub_cords: Tuple[Tuple[int, int]] = (
    (
        0,
        0,
    ),
    (
        0,
        1,
    ),
    (
        0,
        2,
    ),
    (
        1,
        0,
    ),
    (
        1,
        1,
    ),
    (
        1,
        2,
    ),
    (
        2,
        0,
    ),
    (
        2,
        1,
    ),
    (
        2,
        2,
    ),
)


def solution() -> None:
    rows: int
    cols: int
    rows, cols = map(int, input().split())

    matrix: List[List[int]] = list()
    sub_matrixs: List[List[List[int]]] = list()
    sub_scores: List[int] = list()

    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    for x in range(rows - 2):
        for y in range(cols - 2):
            sub_mtrx: List[List[int]] = [
                [
                    0,
                    0,
                    0,
                ],
                [
                    0,
                    0,
                    0,
                ],
                [
                    0,
                    0,
                    0,
                ],
            ]
            sub_score: int = int()
            for sx, sy in sub_cords:
                val: int = matrix[x + sx][y + sy]
                sub_mtrx[sx][sy] = val
                sub_score += val
            sub_matrixs.append(sub_mtrx)
            sub_scores.append(sub_score)

    if DEBUG:
        print(rows, cols, matrix)
        print(sub_matrixs, sub_scores)

    max_score: int = max(sub_scores)
    max_sub_mtrx_index: int = sub_scores.index(max_score)
    max_sub_mtrx: List[List[int]] = sub_matrixs[max_sub_mtrx_index]

    if DEBUG:
        print(max_sub_mtrx_index, max_sub_mtrx, max_score)

    print(f"Sum = {max_score}")
    for row in max_sub_mtrx:
        print(" ".join(map(str, row)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
