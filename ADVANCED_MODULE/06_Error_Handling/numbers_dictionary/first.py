from typing import Dict, Tuple


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
