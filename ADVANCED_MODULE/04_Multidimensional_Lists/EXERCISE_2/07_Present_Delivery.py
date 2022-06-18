from typing import Generator, Callable, Tuple, List, Union, Dict

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "4",
        "- X V -",
        "- S - V",
        "- - - -",
        "X - - -",
        "up",
        "right",
        "down",
        "right",
        "Christmas morning",
    ),
    (
        "3",
        "4",
        "- - - -",
        "V - X -",
        "- V C V",
        "- - - S",
        "left",
        "up",
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
}

PLAYER: str = "S"
COOKIE: str = "C"
NICE: str = "V"
NAUGHTY: str = "X"
EMPTY: str = "-"

around: Tuple[str] = (
    "left",
    "right",
    "up",
    "down",
)


def solution() -> None:
    presents: int = int(input())
    area: int = int(input())

    grid: List[List[str]] = list()

    plr_x: int = int()
    plr_y: int = int()
    new_x: int = int()
    new_y: int = int()

    gifts_given: int = int()

    for _ in range(area):
        grid.append(input().split())

    plr_x, plr_y = find(grid, area, PLAYER)
    cell: str = PLAYER

    nice_count_initial: int = count(grid, area, NICE)

    while presents > 0:
        cmd: str = input()
        if cmd == "Christmas morning":
            break
        move_action: Callable[[int, int], Tuple[int, int]] = move[cmd]
        new_x, new_y = move_action(plr_x, plr_y)
        if valid(area, new_x, new_y):
            cell = grid[new_x][new_y]
            grid[plr_x][plr_y] = EMPTY
            grid[new_x][new_y] = PLAYER
            plr_x, plr_y = new_x, new_y

        if cell == EMPTY:
            pass
        elif cell == PLAYER:
            pass
        elif cell == NAUGHTY:
            pass
        elif cell == NICE:
            gifts_given += 1
            presents -= 1
            if presents == 0:
                break
        elif cell == COOKIE:
            for directon in around:
                x, y = move[directon](plr_x, plr_y)
                if grid[x][y] in [NAUGHTY, NICE] and presents > 0:
                    gifts_given += 1
                    presents -= 1
                    grid[x][y] = EMPTY
        else:
            pass

    nice_count_final: int = count(grid, area, NICE)

    if presents == 0 and nice_count_final > 0:
        print("Santa ran out of presents!")

    for row in grid:
        print(" ".join(row))

    print(
        f"Good job, Santa! {nice_count_initial} happy nice kid/s."
        if nice_count_final == 0
        else f"No presents for {nice_count_final} nice kid/s."
    )


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
