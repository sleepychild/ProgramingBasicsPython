from typing import Generator, Callable, Tuple, Set, Dict, List


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "1 2 3 4 5",
        "1 2 3",
        "3",
        "Add First 5 6",
        "Remove Second 8 9 11",
        "Check Subset",
    ),
    (
        "5 4 2 9 9 5 4",
        "1 1 1 5 6 5",
        "4",
        "Add First 5 6 9 3",
        "Add Second 1 2 3 3 3",
        "Check Subset",
        "Remove Second 1 2 3 4 5",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    first: Set = set(map(int, input().split()))
    second: Set = set(map(int, input().split()))

    for _ in range(int(input())):
        operation, target_name, *nums_tpl = input().split()
        target: Set = locals().get(target_name.lower())
        nums: Set = set(map(int, nums_tpl))
        if operation == "Add":
            target.update(nums)
        elif operation == "Remove":
            target.difference_update(nums)
        else:
            print(first.issubset(second) or second.issubset(first))

    print(", ".join(tuple(map(str, sorted(first)))))
    print(", ".join(tuple(map(str, sorted(second)))))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
