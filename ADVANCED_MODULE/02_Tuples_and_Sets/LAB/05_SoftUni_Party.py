from typing import Generator, Callable, Tuple, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "7IK9Yo0h",
        "9NoBUajQ",
        "Ce8vwPmE",
        "SVQXQCbc",
        "tSzE5t0p",
        "9NoBUajQ",
        "Ce8vwPmE",
        "SVQXQCbc",
        "END",
    ),
    (
        "6",
        "m8rfQBvl",
        "fc1oZCE0",
        "UgffRkOn",
        "7ugX7bm0",
        "9CQBGUeJ",
        "2FQZT3uC",
        "2FQZT3uC",
        "9CQBGUeJ",
        "fc1oZCE0",
        "END",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    codes: Set = set()
    for _ in range(int(input())):
        codes.add(input())
    while True:
        line_in: str = input()
        if line_in == "END":
            break
        codes.remove(line_in)
    print(len(codes))
    for code in sorted(codes):
        print(code)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
