from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "ABC",
        "DEF",
        "X!@",
        "!",
    ),
    (
        "4",
        "asdd",
        "xczc",
        "qwee",
        "qefw",
        "4",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    mtrx_rng: int = int(input())
    matrix: List[List[str]] = list()

    for _ in range(mtrx_rng):
        matrix.append(list(input()))

    if DEBUG:
        print(matrix)

    srch: str = input()
    found: Tuple[int] = tuple()

    for y in range(mtrx_rng):
        for x in range(mtrx_rng):
            if matrix[x][y] == srch:
                found = (
                    x,
                    y,
                )
                break

    # for x, row in enumerate(matrix):
    #     try:
    #         y: int = row.index(srch)
    #     except ValueError as e:
    #         pass
    #     else:
    #         found = (
    #             x,
    #             y,
    #         )

    print(found if found else f"{srch} does not occur in the matrix")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
