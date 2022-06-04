from typing import Generator, Callable, Tuple, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "8",
        "Lee",
        "Joey",
        "Lee",
        "Joe",
        "Alan",
        "Alan",
        "Peter",
        "Joey",
    ),
    (
        "7",
        "Lyle",
        "Bruce",
        "Alice",
        "Easton",
        "Shawn",
        "Alice",
        "Shawn",
    ),
    (
        "6",
        "Adam",
        "Adam",
        "Adam",
        "Adam",
        "Adam",
        "Adam",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    names: Set = set()
    for _ in range(int(input())):
        names.add(input())

    for name in names:
        print(name)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
