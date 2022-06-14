from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3, 6",
        "7, 1, 3, 3, 2, 1",
        "1, 3, 9, 8, 5, 6",
        "4, 6, 7, 9, 1, 0",
    ),
    (
        "2, 4",
        "10, 11, 12, 13",
        "14, 15, 16, 17",
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
        1,
        0,
    ),
    (
        1,
        1,
    ),
)


def solution() -> None:
    rows: int
    cols: int
    rows, cols = map(int, input().split(", "))

    matrix: List[List[int]] = list()
    sub_matrixs: List[List[List[int]]] = list()
    sub_scores: List[int] = list()

    for _ in range(rows):
        matrix.append(list(map(int, input().split(", "))))

    for x in range(rows - 1):
        for y in range(cols - 1):
            sub_mtrx: List[List[int]] = [
                [
                    0,
                    0,
                ],
                [
                    0,
                    0,
                ],
            ]
            sub_score: int = int()
            for sub_cord in sub_cords:
                val: int = matrix[x + sub_cord[0]][y + sub_cord[1]]
                sub_mtrx[sub_cord[0]][sub_cord[1]] = val
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

    for row in max_sub_mtrx:
        print(" ".join(map(str, row)))
    print(max_score)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
