from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "1, 2, 3",
        "4, 5, 6",
        "7, 8, 9",
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
        matrix.append(list(map(int, input().split(", "))))

    prid: List[int] = list()
    secd: List[int] = list()

    for p, s in zip(range(mtrx_size), range(mtrx_size - 1, -1, -1)):
        prid.append(matrix[p][p])
        secd.append(matrix[p][s])

    if DEBUG:
        print(matrix)
        print(prid)
        print(secd)

    print(f"Primary diagonal: {', '.join(map(str, prid))}. Sum: {sum(prid)}")
    print(f"Secondary diagonal: {', '.join(map(str, secd))}. Sum: {sum(secd)}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
