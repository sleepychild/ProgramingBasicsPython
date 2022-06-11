from typing import Generator, Callable, List, Tuple
from os import remove

DEBUG: bool = False


TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "Create-file.txt",
        "Add-file.txt-First Line",
        "Add-file.txt-Second Line",
        "Replace-random.txt-Some-some",
        "Replace-file.txt-First-1st",
        "Replace-file.txt-Second-2nd",
        "Delete-random.txt",
        "Delete-file.txt",
        "End",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def Create(file_name: str) -> None:
    if DEBUG:
        print(f"Create '{file_name}'")
    with open(file_name, "wt") as f:
        pass


def Add(file_name: str, content: str) -> None:
    if DEBUG:
        print(f"Add '{content}' to '{file_name}'")
    with open(file_name, "at") as f:
        f.write(f"{content}\n")


def Replace(file_name: str, old_string: str, new_string: str) -> None:
    if DEBUG:
        print(f"Replace '{old_string}' with '{new_string}'")
    try:
        with open(file_name, "rt") as f:
            file_lines: List[str] = f.readlines()
    except FileNotFoundError as _:
        print("An error occurred")
        return
    for line, file_line in enumerate(file_lines):
        file_lines[line] = file_line.replace(old_string, new_string)
    with open(file_name, "wt") as f:
        f.writelines(file_lines)


def Delete(file_name: str) -> None:
    if DEBUG:
        print(f"Delete '{file_name}'")
    try:
        remove(file_name)
    except FileNotFoundError as _:
        print("An error occurred")


def solution() -> None:
    while not (line_in := input()) == "End":
        command, *args = line_in.split("-")
        globals()[command](*args)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
