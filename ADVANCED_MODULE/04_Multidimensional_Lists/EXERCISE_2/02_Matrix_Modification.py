from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "1 2 3",
        "4 5 6",
        "7 8 9",
        "Add 0 0 5",
        "Subtract 1 1 2",
        "END",
    ),
    (
        "4",
        "1 2 3 4",
        "5 6 7 8",
        "8 7 6 5",
        "4 3 2 1",
        "Add 4 4 100",
        "Add 3 3 100",
        "Subtract -1 -1 42",
        "Subtract 0 0 42",
        "END",
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
    matrix: List[List[int]] = list()

    for _ in range(matrix_size):
        matrix.append(list(map(int, input().split())))

    if DEBUG:
        print(matrix)

    while True:
        cmd, *params = input().split()

        if cmd == "END":
            break

        x, y, p = list(map(int, params))

        if not valid(matrix_size, x, y):
            print("Invalid coordinates")
            continue

        if cmd == "Add":
            matrix[x][y] += p
        elif cmd == "Subtract":
            matrix[x][y] -= p

    for row in matrix:
        print(" ".join(map(str, row)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
