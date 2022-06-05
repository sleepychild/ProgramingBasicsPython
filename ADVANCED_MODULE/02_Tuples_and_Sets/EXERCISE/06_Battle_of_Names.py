from typing import Generator, Callable, Tuple, Set, Dict, List


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4",
        "Pesho",
        "Stefan",
        "Stamat",
        "Gosho",
    ),
    (
        "6",
        "Preslav",
        "Gosho",
        "Ivan",
        "Stamat",
        "Pesho",
        "Stefan",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def process_name(name: str, row: int) -> int:
    return sum(ord(c) for c in name) // row


def solution() -> None:
    odd_set: Set[int] = set()
    even_set: Set[int] = set()

    for i in range(1, int(input()) + 1):
        name_result: int = process_name(input(), i)
        (even_set if (name_result % 2) == 0 else odd_set).add(name_result)

    if DEBUG:
        print(even_set)
        print(odd_set)

    odd_sum: int = sum(odd_set)
    even_sum: int = sum(even_set)

    if odd_sum > even_sum:
        print(", ".join(map(str, odd_set.difference(even_set))))
    elif odd_sum < even_sum:
        print(", ".join(map(str, odd_set.symmetric_difference(even_set))))
    else:
        print(", ".join(map(str, odd_set.union(even_set))))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
