from typing import ClassVar, Generator, Callable, Tuple, List, Dict

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "up right right up right",
        "* * * c *",
        "* * * e *",
        "* * c * *",
        "s * * c *",
        "* * c * *",
    ),
    (
        "4",
        "up right right right down",
        "* * * e",
        "* * c *",
        "* s * c",
        "* * * *",
    ),
    (
        "6",
        "left left down right up left left down down down",
        "* * * * * *",
        "e * * * c *",
        "* * c s * *",
        "* * * * * *",
        "c * * * c *",
        "* * c * * *",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Player:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.coal: int = int()
        self.alive = True

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return " ".join([f"{k}: {v}" for k, v in self.__dict__.items()])

    def __repr__(self) -> str:
        return str(self)


class Grid:
    directions: ClassVar[Dict[str, Tuple[int, int]]] = {
        "up": (
            -1,
            0,
        ),
        "right": (
            0,
            1,
        ),
        "down": (
            1,
            0,
        ),
        "left": (
            0,
            -1,
        ),
    }

    def __init__(self, grid_size: int) -> None:
        self.grid_size: int = grid_size
        self.grid: List[List[int]] = [input().split() for _ in range(self.grid_size)]

        for row in range(grid_size):
            for col in range(grid_size):
                if self.grid[row][col] == "s":
                    self.player: Player = Player(row, col)
                    self.grid[row][col] = "*"

    def valid(self, row: int, col: int) -> bool:
        return all(
            [
                row in range(self.grid_size),
                col in range(self.grid_size),
            ]
        )

    def move(self, direction: str) -> None:
        xd: int
        yd: int
        xd, yd = self.directions[direction]

        xn: int
        yn: int
        xn, yn = self.player.x + xd, self.player.y + yd

        if self.valid(xn, yn):
            self.player.move(xn, yn)
        else:
            return

        collision: str = self.get_collision()

        if collision == "c":
            self.player.coal += 1
            self.grid[xn][yn] = "*"
        elif collision == "e":
            self.player.alive = False

    def get_collision(self) -> str:
        return self.grid[self.player.x][self.player.y]

    def coal_count(self) -> int:
        coal_count: int = int()
        for row in self.grid:
            for col in row:
                if col == "c":
                    coal_count += 1
        return coal_count

    def __str__(self) -> str:
        return "\n".join([f"{' '.join(row)}" for row in self.grid])

    def __repr__(self) -> str:
        return str(self)


def solution() -> None:
    grid_size = int(input())
    player_movements: List[str] = input().split()
    grid: Grid = Grid(grid_size)

    for movement in player_movements:
        if grid.player.alive:
            grid.move(movement)
        else:
            break

    if DEBUG:
        print(grid)
        print(grid.player)

    if not grid.player.alive:
        print(f"Game over! ({grid.player.x}, {grid.player.y})")
    else:
        coal_count: int = grid.coal_count()
        if coal_count > 0:
            print(
                f"{coal_count} pieces of coal left. ({grid.player.x}, {grid.player.y})"
            )
        else:
            print(f"You collected all coal! ({grid.player.x}, {grid.player.y})")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
