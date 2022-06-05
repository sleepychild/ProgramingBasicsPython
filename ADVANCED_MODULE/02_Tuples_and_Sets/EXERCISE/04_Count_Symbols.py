from typing import Generator, Callable, Tuple, Set, List


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("SoftUni rocks",),
    ("Why do you like Python?",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    line_in: str = input()
    line_list: List[str] = list(line_in)
    line_set: Set[str] = set(line_in)

    if DEBUG:
        print(line_in)
        print(line_list)
        print(sorted(line_set))

    for e in sorted(line_set):
        print(f"{e}: {line_list.count(e)} time/s")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
