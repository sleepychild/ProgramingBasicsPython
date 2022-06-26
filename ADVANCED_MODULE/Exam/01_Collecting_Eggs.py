from typing import Generator, Callable, Tuple, Deque
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "20, 13, -7, 7",
        "10, 5, 20, 15, 7, 9",
    ),
    (
        "2, 4, 7, 8, 0",
        "5, 6, 2",
    ),
    (
        "12, 23",
        "28, 40",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    BOX_SIZE: int = 50
    NEXT_EGG: int = 0
    NEXT_PAPER: int = -1

    boxes_filled: int = int()

    eggs: Deque = deque(map(int, input().split(", ")))
    papers: Deque = deque(map(int, input().split(", ")))

    while eggs and papers:
        if eggs[NEXT_EGG] < 1:
            eggs.popleft()
            continue

        if eggs[NEXT_EGG] == 13:
            eggs.popleft()
            papers[0], papers[-1] = papers[-1], papers[0]
            continue

        egg: int = eggs.popleft()
        paper: int = papers.pop()
        boxes_filled += 1 if (egg + paper) <= BOX_SIZE else 0

    if DEBUG:
        print(eggs, papers, boxes_filled)

    if boxes_filled:
        print(f"Great! You filled {boxes_filled} boxes.")
    else:
        print("Sorry! You couldn't fill any boxes!")

    if eggs:
        print(f"Eggs left: {', '.join(map(str, eggs))}")

    if papers:
        print(f"Pieces of paper left: {', '.join(map(str, papers))}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
