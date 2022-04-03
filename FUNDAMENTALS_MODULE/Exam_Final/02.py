from typing import List, Tuple, Generator, Callable


DEBUG: bool = True

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    pass


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
