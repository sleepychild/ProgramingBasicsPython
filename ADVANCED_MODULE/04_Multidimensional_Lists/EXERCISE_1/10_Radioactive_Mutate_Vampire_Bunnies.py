from typing import Generator, Callable, Tuple, List
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5 6",
        ".....P",
        "......",
        "...B..",
        "......",
        "......",
        "ULDDDR",
    ),
    (
        "4 5",
        ".....",
        ".....",
        ".B...",
        "...P.",
        "LLLLLLLL",
    ),
    (
        "5 8",
        ".......B",
        "...B....",
        "....B..B",
        "........",
        "..P.....",
        "ULLL",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Directions(Enum):
    U: Tuple[int, int] = (
        -1,
        0,
    )
    R: Tuple[int, int] = (
        0,
        1,
    )
    D: Tuple[int, int] = (
        1,
        0,
    )
    L: Tuple[int, int] = (
        0,
        -1,
    )


PLAYER_MODEL: str = "P"
BUNNY_MODEL: str = "B"
EMPTY_MODEL: str = "*"


class GameObject:
    def __init__(
        self, gm: "GameManager", x: int, y: int, model: str = EMPTY_MODEL
    ) -> None:
        self.gm: "GameManager" = gm
        self.x: int = x
        self.y: int = y
        self.model: str = model

    def location(self) -> Tuple[int, int]:
        return self.x, self.y

    def next_location(self, dir: Tuple[int, int]) -> Tuple[int, int]:
        xd: int
        yd: int
        xd, yd = dir
        return self.x + xd, self.y + yd

    def __str__(self) -> str:
        return f"{type(self)}: " + " ".join(
            [f"{k}: {v}" for k, v in self.__dict__.items()]
        )

    def __repr__(self) -> str:
        return str(self)


class Enemy(GameObject):
    def update(self) -> None:
        pass


class Bunny(Enemy):
    def __init__(
        self, gm: "GameManager", x: int, y: int, model: str = BUNNY_MODEL
    ) -> None:
        super().__init__(gm, x, y, model)
        self.active: bool = True

    def update(self) -> None:
        if self.active:
            for spawn_location in [
                self.next_location(Directions[d].value) for d in list("UDLR")
            ]:
                if self.gm.grid.valid(*spawn_location) and (
                    not spawn_location
                    in [enemy.location() for enemy in self.gm.enemies]
                ):
                    self.gm.enemies.append(Bunny(self.gm, *spawn_location))
            self.active = False


class Player(GameObject):
    def __init__(
        self,
        gm: "GameManager",
        x: int,
        y: int,
        movements: List[Tuple[int, int]],
        model: str = PLAYER_MODEL,
    ) -> None:
        super().__init__(gm, x, y, model)
        self.movements: Generator[Tuple[int, int], None, None] = (m for m in movements)
        self.alive: bool = True
        self.escaped: bool = False

    def update(self) -> None:
        if self.alive and (not self.escaped):
            try:
                next_location: Tuple[int, int] = self.next_location(
                    next(self.movements)
                )
            except StopIteration as e:
                if DEBUG:
                    print(e)
                    raise
            else:
                if self.gm.grid.valid(*next_location):
                    self.move(*next_location)
                else:
                    self.escaped = True

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Grid:
    def __init__(self, gm: "GameManager", rows: int, cols: int) -> None:
        self.gm: "GameManager" = gm

        self.rows: int = rows
        self.cols: int = cols
        self.grid: List[List[str]] = [list(input()) for _ in range(self.rows)]

    def blank_grid(self) -> List[List[str]]:
        return [["." for c in range(self.cols)] for r in range(self.rows)]

    def update(self) -> None:
        new_grid: List[List[str]] = self.blank_grid()
        if not self.gm.player.escaped:
            px, py = self.gm.player.location()
            new_grid[px][py] = self.gm.player.model
        for enemy in self.gm.enemies:
            ex, ey = enemy.location()
            new_grid[ex][ey] = enemy.model
        self.grid = new_grid

    def valid(self, row: int, col: int) -> bool:
        return all(
            [
                row in range(self.rows),
                col in range(self.cols),
            ]
        )

    def get_objects_locations(self, mark: str) -> List[Tuple[int, int]]:
        objects_locations: List[Tuple[int, int]] = list()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == mark:
                    objects_locations.append(
                        (
                            row,
                            col,
                        )
                    )
        return objects_locations

    def __str__(self) -> str:
        return "\n".join([f"{''.join(row)}" for row in self.grid])

    def __repr__(self) -> str:
        return str(self)


class GameManager:
    def __init__(self) -> None:
        rows: int
        cols: int
        rows, cols = map(int, input().split())
        self.grid: Grid = Grid(self, rows, cols)

        player_movements: List[Tuple[int, int]] = [
            Directions[d].value for d in list(input())
        ]
        self.player: Player = Player(
            self, *self.grid.get_objects_locations(PLAYER_MODEL)[0], player_movements
        )

        self.enemies: List[Enemy] = list()
        for enemy_location in self.grid.get_objects_locations(BUNNY_MODEL):
            self.enemies.append(Bunny(self, *enemy_location))

    def run(self) -> None:
        while self.player.alive and not self.player.escaped:
            self.update()
            self.collide()

    def update(self) -> None:
        self.player.update()
        active_enemies: List[Enemy] = list(filter(lambda e: e.active, self.enemies))
        for enemy in active_enemies:
            enemy.update()
        self.grid.update()

    def collide(self) -> None:
        if not self.player.escaped and self.player.location() in [
            enemy.location() for enemy in self.enemies
        ]:
            self.player.alive = False

    def draw(self) -> None:
        print(self.grid)
        print(self.player)
        for i, enemy in enumerate(self.enemies):
            print(i, enemy)


def solution() -> None:
    gm: GameManager = GameManager()
    gm.run()
    print(gm.grid)
    print("won:" if gm.player.alive else "dead:", f"{gm.player.x} {gm.player.y}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
