from typing import Generator, Callable, Tuple, Dict


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "one",
        "1",
        "two",
        "2",
        "Search",
        "one",
        "Remove",
        "two",
        "End",
    ),
    (
        "one",
        "two",
        "Search",
        "Remove",
        "End",
    ),
    (
        "one",
        "1",
        "Search",
        "one",
        "Remove",
        "two",
        "End",
    ),
    (
        "Search",
        "Remove",
        "End",
    ),
    (
        "one",
        "1",
        "two",
        "2",
        "two point five",
        "2.5",
        "twenty five",
        "25",
        "Search",
        "one",
        "two",
        "two point five",
        "Remove",
        "two point five",
        "two",
        "End",
    ),
    (
        "one",
        "1",
        "two",
        "2",
        "Search",
        "one",
        "two",
        "Insert",
        "ten",
        "10",
        "twenty",
        "20",
        "Remove",
        "two",
        "ten",
        "Fifty",
        "Search",
        "one",
        "End",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


# Due to garbo task definition we have two solutions

# First solution

# Output:
# 1
# {'one': 1}
# The variable number must be an integer
# {}
# 1
# Number does not exist in dictionary
# {'one': 1}
# {}
# The variable number must be an integer
# 1
# 2
# Number does not exist in dictionary
# Number does not exist in dictionary
# {'one': 1, 'twenty five': 25}


def insert(nums_dict: Dict[str, int], key: str, val: str) -> None:
    try:
        nums_dict[key] = int(val)
    except ValueError as _:
        print("The variable number must be an integer")


def search(nums_dict: Dict[str, int], key: str) -> None:
    try:
        print(nums_dict[key])
    except KeyError as _:
        print("Number does not exist in dictionary")


def remove(nums_dict: Dict[str, int], key: str) -> None:
    try:
        del nums_dict[key]
    except KeyError as _:
        print("Number does not exist in dictionary")


def solution() -> None:
    modes: Tuple[str] = (
        "Insert",
        "Search",
        "Remove",
        "End",
    )
    mode: str = "Insert"
    numbers_dictionary: Dict[str, int] = dict()

    while mode != "End":
        if (line_in := input()) in modes:
            mode = line_in
            continue
        elif mode == "Insert":
            insert(numbers_dictionary, line_in, input())
        elif mode == "Search":
            search(numbers_dictionary, line_in)
        elif mode == "Remove":
            remove(numbers_dictionary, line_in)
        else:
            break

    print(numbers_dictionary)


# Second solution

# Output:
# 1
# {'one': 1}
# The variable number must be an integer
# {}
# 1
# Number does not exist in dictionary
# {'one': 1}
# {}
# The variable number must be an integer
# {'one': 1, 'two': 2}


def alt_solution() -> None:
    numbers_dictionary: Dict[str, int] = dict()

    try:
        while (line_in := input()) != "Search":
            numbers_dictionary[line_in] = int(input())
        while (line_in := input()) != "Remove":
            print(numbers_dictionary[line_in])
        while (line_in := input()) != "End":
            del numbers_dictionary[line_in]
    except ValueError as _:
        print("The variable number must be an integer")
    except KeyError as _:
        print("Number does not exist in dictionary")

    print(numbers_dictionary)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        alt_solution()
else:
    solution()
