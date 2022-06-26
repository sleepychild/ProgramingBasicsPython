from typing import Generator, Callable, List, Tuple

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "Tom, Jerry",
        ". . T . . .",
        ". . . . . .",
        ". . W . . .",
        ". . W . . E",
        ". . . . . .",
        ". T . W . .",
        "(3, 2)",
        "(1, 3)",
        "(5, 1)",
        "(5, 1)",
    ),
    (
        "Jerry, Tom",
        ". T . . . W",
        ". . . . T .",
        ". W . . . T",
        ". T . E . .",
        ". . . . . T",
        ". . T . . .",
        "(1, 1)",
        "(3, 0)",
        "(3, 3)",
    ),
    (
        "Jerry, Tom",
        ". . . W . .",
        ". . T T . .",
        ". . . . . .",
        ". T . W . .",
        "W . . . E .",
        ". . . W . .",
        "(0, 3)",
        "(3, 3)",
        "(1, 3)",
        "(2, 2)",
        "(3, 5)",
        "(4, 0)",
        "(5, 3)",
        "(3, 1)",
        "(4, 4)",
        "(4, 4)",
    ),
    (),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


AREA: int = 6
EXIT: str = "E"
TRAP: str = "T"
WALL: str = "W"
EMPTY: str = "."


def solution() -> None:

    players: List = input().split(", ")
    grid: List[List[str]] = list()

    rest: List[str] = list()

    for _ in range(AREA):
        grid.append(input().split())

    play = True

    while play:
        for plr_id, plr in enumerate(players):

            if play == False:
                break

            x, y = map(int, input()[1:-1].split(", "))
            pos = grid[x][y]

            # if DEBUG:
            #     print(plr, x, y, pos, rest)

            if plr in rest:
                rest.remove(plr)
            elif pos == WALL:
                print(f"{plr} hits a wall and needs to rest.")
                rest.append(plr)
            elif pos == TRAP:
                play = False
                print(f"{plr} is out of the game! The winner is {players[plr_id-1]}.")
            elif pos == EXIT:
                play = False
                print(f"{plr} found the Exit and wins the game!")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
