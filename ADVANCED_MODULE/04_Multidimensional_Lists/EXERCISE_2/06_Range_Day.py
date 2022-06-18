from typing import Generator, Callable, Tuple, List, Union, Dict

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        ". . . . .",
        "x . . . .",
        ". A . . .",
        ". . . x .",
        ". x . . x",
        "3",
        "shoot down",
        "move right 4",
        "move left 1",
    ),
    (
        ". . . . .",
        ". . . . .",
        ". A x . .",
        ". . . . .",
        ". x . . .",
        "2",
        "shoot down",
        "shoot right",
    ),
    (
        ". . . . .",
        ". . . . .",
        ". . x . .",
        ". . . . .",
        ". x . . A",
        "3",
        "shoot down",
        "move right 2",
        "shoot left",
    ),
    (
        "x . . . x",
        ". . x . .",
        ". . . . .",
        ". . A . .",
        "x . . . x",
        "4",
        "move up 2",
        "move up 1",
        "move up 1",
        "move up 2",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def valid(area: int, x: int, y: int) -> bool:
    return all(
        [
            x in range(area),
            y in range(area),
        ]
    )


def find(grid: List[List[str]], area: int, mark: str) -> Union[Tuple[int, int], bool]:
    for x in range(area):
        for y in range(area):
            if grid[x][y] == mark:
                return x, y
    return False


def count(grid: List[List[str]], area: int, mark: str) -> int:
    res: int = int()
    for x in range(area):
        for y in range(area):
            if grid[x][y] == mark:
                res += 1
    return res


def print_grid(grid: List[List[str]], area: int) -> None:
    brdr: str = "-" * (area * 2 - 1)
    print(f"+{brdr}+")
    for row in grid:
        print(f"|{' '.join(row)}|")
    print(f"+{brdr}+")


move: Dict[str, Callable[[int, int, int], Tuple[int, int]]] = {
    "up": lambda x, y, d=1: (x - d, y),
    "down": lambda x, y, d=1: (x + d, y),
    "left": lambda x, y, d=1: (x, y - d),
    "right": lambda x, y, d=1: (x, y + d),
    "up_r": lambda x, y, d=1: (x + d, y),
    "down_r": lambda x, y, d=1: (x - d, y),
    "left_r": lambda x, y, d=1: (x, y + d),
    "right_r": lambda x, y, d=1: (x, y - d),
}

PLAYER: str = "A"
TARGET: str = "x"
EMPTY: str = "."


def solution() -> None:
    area: int = 5
    grid: List[List[str]] = list()

    plr_x: int = int()
    plr_y: int = int()
    new_x: int = int()
    new_y: int = int()

    hits: List[List[int, int]] = list()

    for _ in range(area):
        grid.append(input().split())

    plr_x, plr_y = find(grid, area, "A")

    if DEBUG:
        print("PLR", plr_x, plr_y)
        print_grid(grid, area)

    for _ in range(int(input())):
        targets_left: int = count(grid, area, TARGET)

        if targets_left < 1:
            break

        cmd, direction, *params = input().split()
        distance: int = int(params[0]) if params else int()
        move_action: Callable[[int, int], Tuple[int, int]] = move[
            f"{direction}_r" if 0 > distance else direction
        ]

        if cmd == "move" and distance != 0:
            new_x, new_y = move_action(plr_x, plr_y, abs(distance))
            if valid(area, new_x, new_y) and grid[new_x][new_y] == EMPTY:
                grid[plr_x][plr_y] = EMPTY
                plr_x, plr_y = new_x, new_y
                grid[new_x][new_y] = PLAYER
                if DEBUG:
                    print_grid(grid, area)

        elif cmd == "shoot":
            new_x, new_y = move_action(plr_x, plr_y)
            while valid(area, new_x, new_y):
                if grid[new_x][new_y] == TARGET:
                    hits.append([new_x, new_y])
                    grid[new_x][new_y] = EMPTY
                    break
                new_x, new_y = move_action(new_x, new_y)
            if DEBUG:
                print_grid(grid, area)

    targets_left: int = count(grid, area, TARGET)

    print(
        f"Training not completed! {targets_left} targets left."
        if targets_left > 0
        else f"Training completed! All {len(hits)} targets hit."
    )

    if hits:
        print("\n".join(map(str, hits)))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
