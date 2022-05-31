from typing import Deque, Tuple, Generator, Callable, List
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    ("{[()]}",),
    ("{[(])}",),
    ("{{[[(())]]}}",),
    ("{{[[(())]]}",),
    ("))]]}}",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    lin: List[str] = list(input())

    parentheses: Deque[int] = deque()
    balanced: bool = True

    if DEBUG:
        print(lin)

    for l in lin:
        if l in (
            "{",
            "[",
            "(",
        ):
            parentheses.append(l)
        elif l in (
            "}",
            "]",
            ")",
        ):
            try:
                if parentheses.pop() != ("{" if l == "}" else "[" if l == "]" else "("):
                    balanced = False
                    break
            except IndexError as _:
                balanced = False
                break


    print("YES" if balanced and not parentheses else "NO")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
