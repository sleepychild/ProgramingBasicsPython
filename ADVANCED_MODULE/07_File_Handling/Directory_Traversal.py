from typing import Generator, Callable, Tuple, List
from os import scandir, path

DEBUG: bool = False


TEST_RUNS: Tuple[Tuple[str]] = (
    ("..",),
    (".",),
    ("files",),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def get_file_list(scan_path: str = ".", depth: int = 1) -> List[str]:
    if DEBUG:
        print(f"Scaning: {scan_path}")
    if depth < 0:
        return list()
    file_list: List[str] = list()
    for entry in scandir(scan_path):
        if entry.is_dir():
            file_list.extend(get_file_list(path.join(scan_path, entry.name), depth - 1))
        if entry.is_file():
            file_list.append(entry.name)
    return file_list


# abcdefghijklmnopqrstuvwxyz


def solution() -> None:
    file_list: List[str] = get_file_list(target_dir := input(), 1)
    file_list.sort()
    file_list.sort(key=lambda x: x.split(".")[-1])
    with open(path.join(target_dir, "report.txt"), "wt") as rep_file:
        extension: str = ""
        for file in file_list:
            if extension != (file_extension := file.split(".")[-1]):
                extension = file_extension
                rep_file.write(f".{extension}\n")
            rep_file.write(f"- - - {file}\n")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
