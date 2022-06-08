from typing import Dict


def solution() -> None:
    global input
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
