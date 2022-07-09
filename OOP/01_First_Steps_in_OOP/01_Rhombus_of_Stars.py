from typing import Tuple, Generator, Callable, List


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = tuple([tuple([str(x)]) for x in range(5)])


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def rhombus(
    size: int,
    symbol: str = "*",
    delimiter: str = " ",
) -> str:
    canvas_width: int = ((len(delimiter) * size) + size) - 1
    return "\n".join(
        [
            delimiter.join([symbol] * (size - abs(count))).center(canvas_width)
            for count in range(-size + 1, size)
        ]
    )


def solution():
    print(rhombus(int(input())))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
