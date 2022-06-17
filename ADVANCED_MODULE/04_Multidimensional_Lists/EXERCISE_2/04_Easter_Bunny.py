from typing import Generator, Callable, Tuple, Union, List, Dict, Any
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "1 3 7 9 11",
        "X 5 4 X 63",
        "7 3 21 95 1",
        "B 1 73 4 9",
        "9 2 33 2 0",
    ),
    (
        "8",
        "4 18 9 7 24 41 52 11",
        "54 21 19 X 6 34 75 57",
        "76 67 7 44 76 27 56 37",
        "92 35 25 37 52 34 56 72",
        "35 X 1 45 4 X 37 63",
        "105 X B 2 12 43 5 19",
        "48 19 35 20 32 27 42 4",
        "73 88 78 32 37 52 X 22",
    ),
    ("0",),
    (
        "1",
        "B",
    ),
    (
        "3",
        "B -1 -2",
        "5 1 1",
        "-1 1 1",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Directions(Enum):
    up: Tuple[int, int] = (
        -1,
        0,
    )
    down: Tuple[int, int] = (
        1,
        0,
    )
    left: Tuple[int, int] = (
        0,
        -1,
    )
    right: Tuple[int, int] = (
        0,
        1,
    )


def valid(size: int, loc: Tuple[int, int]) -> bool:
    return all(
        [
            loc[0] in range(size),
            loc[1] in range(size),
        ]
    )


def move(loc: Tuple[int, int], vel: Tuple[int, int]) -> Tuple[int, int]:
    return loc[0] + vel[0], loc[1] + vel[1]


def get_value(
    grid: List[List[Union[str, int]]], loc: Tuple[int, int]
) -> Union[int, str]:
    return grid[loc[0]][loc[1]]


def get_start(
    size: int, grid: List[List[Union[str, int]]]
) -> Union[Tuple[int, int], None]:
    for x in range(size):
        for y in range(size):
            if grid[x][y] == "B":
                return x, y


def solution():
    size: int = int(input())
    grid: List[List[Union[str, int]]] = list()

    for x in range(size):
        grid.append(list())
        for e in input().split():
            grid[x].append(e if e.isalpha() else int(e))

    start: Union[Tuple[int, int], None] = get_start(size, grid)

    collected: List = list()

    for direction in Directions:
        direction_data: Dict = {
            "name": direction.name,
            "loc": list(),
            "val": list(),
            "sum": int(),
        }
        try:
            location: Tuple[int, int] = move(start, direction.value)
        except TypeError as _:
            break
        while valid(size, location):
            value: Any = get_value(grid, location)
            if value == "X":
                break
            direction_data["loc"].append(
                [
                    location[0],
                    location[1],
                ]
            )
            direction_data["val"].append(get_value(grid, location))
            direction_data["sum"] = sum(direction_data["val"])
            location = move(location, direction.value)
        collected.append(direction_data)

    if DEBUG:
        for path in collected:
            print(path)

    collected.sort(key=lambda x: len(x["loc"]), reverse=True)
    collected.sort(key=lambda x: x["sum"], reverse=True)

    if DEBUG:
        print("\n".join([" ".join([str(r) for r in row]) for row in grid]))
        for path in collected:
            print(path)

    if collected:
        best_path: List[Dict] = collected[0]
        print(best_path["name"])
        tuple(map(print, best_path["loc"]))
        print(best_path["sum"])


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
