from typing import Generator, Callable, Tuple, List, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "1 5 4 2 2 3 1 3 2",
        "4",
    ),
    (
        "11 8 5 6 9 2 9 7 3 4",
        "11",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    numbers: List[int] = list(map(int, input().split()))
    target: int = int(input())

    iterations: int = int()
    combinations: Set = set()

    if DEBUG:
        print(numbers)
        print(target)

    for i, a in enumerate(numbers):
        for b in numbers[i + 1 :]:
            iterations += 1
            if a + b == target:
                print(f"{a} + {b} = {target}")
                combinations.add(
                    (
                        a,
                        b,
                    )
                )

    print(f"Iterations done: {iterations}")
    for combination in combinations:
        print(combination)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
