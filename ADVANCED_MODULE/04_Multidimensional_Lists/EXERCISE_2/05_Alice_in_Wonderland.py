from typing import Generator, Callable, Tuple, Union, List
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        ". A . . 1",
        "R . 2 . .",
        "4 7 . 1 .",
        ". . . 2 .",
        ". 3 . . .",
        "down",
        "right",
        "left",
        "down",
        "up",
        "left",
    ),
    (
        "7",
        ". A . 1 1 . .",
        "9 . . . 6 . 5",
        ". 6 . R . . .",
        ". 3 . . 1 . .",
        ". . . 2 . . 2",
        ". 3 . . 1 . .",
        ". 8 3 . . . 2",
        "left",
        "down",
        "down",
        "right",
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


class Location:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __add__(self, other) -> "Location":
        if hasattr(other, "x") and hasattr(other, "y"):
            return Location(self.x + other.x, self.y + other.y)
        else:
            return Location(self.x + other[0], self.y + other[1])

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y}"

    def __repr__(self) -> str:
        return str(self)


class Player:
    def __init__(self, parent: "GameManager", loc: Location) -> None:
        self.gm = parent
        self.loc: Location = loc
        self.alive: bool = True
        self.score: int = int()
        self.gm.grid.set_cell(self.loc, "*")

    def update(self) -> None:
        next_loc: Location = self.loc + Directions[input()].value
        if not self.gm.grid.valid(next_loc):
            self.alive = False
            return
        self.loc = next_loc
        collider: Union[str, int] = self.gm.grid.get_cell(self.loc)
        self.gm.grid.set_cell(self.loc, "*")
        if collider == "R":
            self.alive = False
            return
        if type(collider) == int:
            self.score += collider

    def __str__(self) -> str:
        return f"Player -> {self.loc} score: {self.score} alive: {self.alive}"

    def __repr__(self) -> str:
        return str(self)


class Grid:
    def __init__(
        self,
        parent: "GameManager",
        rows: int,
        cols: int,
        grid: List[List[Union[str, int]]],
    ) -> None:
        self.gm = parent
        self.rows: int = rows
        self.cols: int = cols
        self.grid: List[List[Union[str, int]]] = grid

    def set_cell(self, loc: Location, model: Union[str, int] = ".") -> None:
        self.grid[loc.x][loc.y] = model

    def get_cell(self, loc: Location) -> Union[str, int]:
        return self.grid[loc.x][loc.y]

    def valid(self, loc: Location) -> bool:
        return all(
            [
                loc.x in range(self.rows),
                loc.y in range(self.cols),
            ]
        )

    def get_objects_locations(self, mark: str) -> List[Location]:
        objects_locations: List[Location] = list()
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] == mark:
                    objects_locations.append(Location(x, y))
        return objects_locations

    def __str__(self) -> str:
        return "\n".join([f"{' '.join(str(r) for r in row)}" for row in self.grid])

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def from_input(cls: "Grid", parent: "GameManager") -> "Grid":
        size: int = int(input())
        grid: List[List[Union[str, int]]] = list()
        for x in range(size):
            grid.append(list())
            for e in input().split():
                try:
                    v: int = int(e)
                except ValueError as _:
                    grid[x].append(e)
                else:
                    grid[x].append(v)
        return Grid(parent, size, size, grid)


class GameManager:
    def __init__(self) -> None:
        self.grid: Grid = Grid.from_input(self)
        self.player: Player = Player(self, self.grid.get_objects_locations("A")[0])

    def run(self) -> None:
        while self.player.alive and self.player.score < 10:
            self.update()
            if DEBUG:
                self.draw()

    def update(self) -> None:
        self.player.update()

    def draw(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.grid}\n{self.player}"

    def __repr__(self) -> str:
        return str(self)


def solution():
    gm: GameManager = GameManager()
    gm.run()
    print(
        "She did it! She went to the party."
        if gm.player.alive
        else "Alice didn't make it to the tea party."
    )
    print(gm.grid)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
