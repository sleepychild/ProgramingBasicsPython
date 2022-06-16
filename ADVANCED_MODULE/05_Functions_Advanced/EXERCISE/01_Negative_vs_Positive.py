from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("1 2 -3 -4 65 -98 12 57 -84",),
    ("1 2 3",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    nums: List[int] = list(map(int, input().split()))
    negative_sum: int = sum(filter(lambda x: x < 0, nums))
    positive_sum: int = sum(filter(lambda x: x > 0, nums))
    pos_neg: bool = positive_sum > abs(negative_sum)

    print(negative_sum)
    print(positive_sum)
    print(
        f"The {'positives' if pos_neg else 'negatives'} are stronger than the {'negatives' if pos_neg else 'positives'}"
    )


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
