from typing import Generator, Callable, Tuple, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4 3",
        "1",
        "3",
        "5",
        "7",
        "3",
        "4",
        "5",
    ),
    (
        "2 2",
        "1",
        "3",
        "1",
        "5",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    n, m = tuple(map(int, input().split()))
    n_set: Set = set()
    for _ in range(n):
        n_set.add(int(input()))
    m_set: Set = set()
    for _ in range(m):
        m_set.add(int(input()))
    tuple(map(print, n_set & m_set))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
