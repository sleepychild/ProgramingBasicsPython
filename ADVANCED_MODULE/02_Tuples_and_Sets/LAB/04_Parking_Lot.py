from typing import Generator, Callable, Tuple, Set


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "10",
        "IN, CA2844AA",
        "IN, CA1234TA",
        "OUT, CA2844AA",
        "IN, CA9999TT",
        "IN, CA2866HI",
        "OUT, CA1234TA",
        "IN, CA2844AA",
        "OUT, CA2866HI",
        "IN, CA9876HH",
        "IN, CA2822UU",
    ),
    (
        "4",
        "IN, CA2844AA",
        "IN, CA1234TA",
        "OUT, CA2844AA",
        "OUT, CA1234TA",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    cars: Set = set()
    for _ in range(int(input())):
        action, reg = input().split(", ")
        if action == "IN":
            cars.add(reg)
        elif action == "OUT":
            cars.remove(reg)
    if cars:
        for reg in cars:
            print(reg)
    else:
        print("Parking Lot is Empty")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
