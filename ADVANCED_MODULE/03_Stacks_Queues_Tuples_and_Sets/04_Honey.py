from collections import deque
from typing import Generator, Callable, Tuple, Deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "20 62 99 35 0 150",
        "120 60 10 1 70 10",
        "+ - + + / * - - /",
    ),
    (
        "30",
        "15 9 5 150 8",
        "* + + * -",
    ),
    (
        "0 0 0 0",
        "1 1 1 1",
        "+ - * / + - * / + - * /",
    ),
    (
        "-1 -1 -1 -1",
        "0 0 0 0",
        "/ / / /",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    bees: Deque[int] = deque(map(int, input().split()))
    nectars: Deque[int] = deque(map(int, input().split()))
    ops: Deque[str] = deque(input().split())

    honey_made: int = int()

    if DEBUG:
        print(bees, nectars, ops)

    while all(
        (
            bees,
            nectars,
            ops,
        )
    ):
        if not bees[0] > nectars[-1]:
            evaluation: str = f"{bees.popleft()} {ops.popleft()} {nectars.pop()}"
            try:
                evaluation_result: int = eval(evaluation)
            except ZeroDivisionError as e:
                if DEBUG:
                    print(e, evaluation)
            else:
                honey_made += abs(evaluation_result)
                if DEBUG:
                    print(f"{evaluation} = {evaluation_result}")

        else:
            nectars.pop()

        if DEBUG:
            print(bees, nectars, ops)

    print(f"Total honey made: {honey_made}")
    if bees:
        print("Bees left:", ", ".join(map(str, bees)))
    if nectars:
        print("Nectar left:", ", ".join(map(str, nectars)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
