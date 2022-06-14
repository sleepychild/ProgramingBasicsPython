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
        "4",
        "-7 14 9 -20",
        "3 4 9 21",
        "-14 6 8 44",
        "30 9 7 -14",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    mtrx_size: int = int(input())
    matrix: List[List[int]] = list()
    for _ in range(mtrx_size):
        matrix.append(list(map(int, input().split())))

    prid: List[int] = list()
    secd: List[int] = list()

    for p, s in zip(range(mtrx_size), range(mtrx_size - 1, -1, -1)):
        prid.append(matrix[p][p])
        secd.append(matrix[p][s])

    if DEBUG:
        print(matrix)
        print(prid)
        print(secd)

    print(abs(sum(prid) - sum(secd)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
