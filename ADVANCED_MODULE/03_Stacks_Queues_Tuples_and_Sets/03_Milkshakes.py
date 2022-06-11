from collections import deque
from typing import Generator, Callable, Tuple, Deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "20, 24, -5, 17, 22, 60, 26",
        "26, 60, 22, 17, 24, 10, 55",
    ),
    (
        "-10, -2, -30, 10",
        "-5",
    ),
    (
        "2, 3, 3, 7, 2",
        "2, 7, 3, 3, 2, 14, 6",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    chocolates: Deque[int] = deque(map(int, input().split(", ")))
    milks: Deque[int] = deque(map(int, input().split(", ")))
    milkshakes: int = int()

    while True:

        if chocolates and chocolates[-1] <= 0:
            chocolates.pop()
            continue

        if milks and milks[0] <= 0:
            milks.popleft()
            continue

        if chocolates and milks:
            if chocolates[-1] == milks[0]:
                milkshakes += 1
                chocolates.pop()
                milks.popleft()
            else:
                chocolates[-1] -= 5
                milks.rotate(-1)

        if DEBUG:
            print(milkshakes, chocolates, milks)

        if not all(
            (
                chocolates,
                milks,
                milkshakes < 5,
            )
        ):
            break

    if DEBUG:
        print(milkshakes, chocolates, milks)

    print(
        "Great! You made all the chocolate milkshakes needed!"
        if milkshakes == 5
        else "Not enough milkshakes."
    )
    print("Chocolate:", ", ".join(map(str, chocolates)) if chocolates else "empty")
    print("Milk:", ", ".join(map(str, milks)) if milks else "empty")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
