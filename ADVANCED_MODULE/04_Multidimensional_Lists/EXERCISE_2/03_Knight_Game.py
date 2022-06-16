from typing import Generator, Callable, Tuple, List

DEBUG: bool = True

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "0K0K0",
        "K000K",
        "00K00",
        "K000K",
        "0K0K0",
    ),
    (
        "2",
        "KK",
        "KK",
    ),
    (
        "8",
        "0K0KKK00",
        "0K00KKKK",
        "00K0000K",
        "KKKKKK0K",
        "K0K0000K",
        "KK00000K",
        "00K0K000",
        "000K00KK",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def valid(size: int, x: int, y: int) -> bool:
    return all(
        [
            x in range(size),
            y in range(size),
        ]
    )


def solution() -> None:
    matrix_size: int = int(input())
    matrix: List[List[str]] = list()

    for _ in range(matrix_size):
        matrix.append(input().split())

    if DEBUG:
        for row in matrix:
            print(" ".join(row))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
