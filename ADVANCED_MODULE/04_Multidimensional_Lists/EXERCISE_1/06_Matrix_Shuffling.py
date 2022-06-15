from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "2 3",
        "1 2 3",
        "4 5 6",
        "swap 0 0 1 1",
        "swap 10 9 8 7",
        "swap 0 1 1 0",
        "END",
    ),
    (
        "2 3",
        "1 2 3",
        "4 5 6",
        "swap 0 0 1 1",
        "swap 10 9 8 7",
        "swap 0 1 1 0",
        "swap 0 1 1",
        "END",
    ),
    (
        "1 2",
        "Hello World",
        "0 0 0 1",
        "swap 0 0 0 1",
        "swap 0 1 0 0",
        "END",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    rows: int
    cols: int

    rows, cols = map(int, input().split())

    matrix: List[List[str]] = list()

    for _ in range(rows):
        matrix.append(input().split())

    if DEBUG:
        print(rows, cols)
        print(matrix)

    while True:
        cmd: str
        cords: List[str]
        cmd, *cords = input().split()

        if DEBUG:
            print(cmd, cords)

        if cmd == "END":
            break
        elif cmd == "swap":
            fx: int
            fy: int
            tx: int
            ty: int

            try:
                fx, fy, tx, ty = [int(c) for c in cords]
            except ValueError as _:
                print("Invalid input!")
                continue
            else:
                if not all(
                    [
                        fx in range(rows),
                        fy in range(cols),
                        tx in range(rows),
                        ty in range(cols),
                    ]
                ):
                    print("Invalid input!")
                    continue

            if DEBUG:
                print(fx, fy, tx, ty)

            matrix[tx][ty], matrix[fx][fy] = matrix[fx][fy], matrix[tx][ty]

            for row in matrix:
                print(" ".join(map(str, row)))

        else:
            print("Invalid input!")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
