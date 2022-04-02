from typing import List, Tuple, Generator, Callable


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '.',
        '@',
        'dsg12gr5653feee5',
    ),
    (
        '?',
        'E',
        '@ABCEF',
    ),
    (
        'a',
        'a',
        'AaBbAaCcDdAa',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    a, b = ord(input()), ord(input())
    print(sum([o for o in [ord(o) for o in input()] if o in range(min(a, b)+1, max(a, b))]))
    # a, b = ord(input()), ord(input())
    # ord_range: range = range(min(a, b)+1, max(a, b))
    # ord_list: List[int] = [ord(o) for o in list(input())]
    # ord_found: List[int] = [o for o in ord_list if o in ord_range]
    # if DEBUG:
    #     print({chr(o): o for o in ord_range})
    #     print({chr(o): o for o in ord_list})
    #     print({chr(o): o for o in ord_found})
    # if a == b:
    #     print(a*ord_list.count(a))
    # else:
    #     print(sum(ord_found))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
