from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3 4",
        "A B B D",
        "E B B B",
        "I J B B",
    ),
    (
        "2 2",
        "a b",
        "c d",
    ),
    (
        "5 4",
        "A A B D",
        "A A B B",
        "I J B B",
        "C C C G",
        "C C K P",
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
    rows, cols = map(int, input().split())
    matrix: List[List[str]] = list()
    found: int = int()

    for _ in range(rows):
        matrix.append(input().split())

    for x in range(rows - 1):
        for y in range(cols - 1):
            found += (
                1
                if len(set([matrix[x + sx][y + sy] for sx, sy in sub_cords])) == 1
                else 0
            )
            if DEBUG:
                for s_x, s_y in sub_cords:
                    print(matrix[x + s_x][y + s_y], end=" ")
                print("")
    print(found)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
