from typing import Generator, Callable, Tuple, Type, List, Dict
from enum import Enum

DEBUG: bool = True

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
    # (
    #     ". . . . .",
    #     ". . . . .",
    #     ". A x . .",
    #     ". . . . .",
    #     ". x . . .",
    #     "2",
    #     "shoot down",
    #     "shoot right",
    # ),
    # (
    #     ". . . . .",
    #     ". . . . .",
    #     ". . x . .",
    #     ". . . . .",
    #     ". x . . A",
    #     "3",
    #     "shoot down",
    #     "move right 2",
    #     "shoot left",
    # ),
    # (
    #     ". . . x x",
    #     ". . . . .",
    #     ". . x x .",
    #     ". . . . .",
    #     "x x . . A",
    #     "8",
    #     "shoot left",
    #     "shoot left",
    #     "shoot up",
    #     "move left 1",
    #     "shoot up",
    #     "shoot up",
    #     "move left 1",
    #     "shoot up",
    # ),
    # (
    #     ". . x . .",
    #     ". . x . .",
    #     "x x A x x",
    #     ". . x . .",
    #     ". . x . .",
    #     "9",
    #     "shoot up",
    #     "shoot up",
    #     "shoot down",
    #     "shoot down",
    #     "shoot left",
    #     "shoot left",
    #     "shoot right",
    #     "shoot right",
    #     "move up 10",
    # ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Location:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y

    def __add__(self, other) -> "Location":
        if hasattr(other, "x") and hasattr(other, "y"):
            return Location(self.x + other.x, self.y + other.y)
        else:
            return Location(self.x + other[0], self.y + other[1])

    def __sub__(self, other) -> "Location":
        if hasattr(other, "x") and hasattr(other, "y"):
            return Location(self.x - other.x, self.y - other.y)
        else:
            return Location(self.x - other[0], self.y - other[1])

    def __eq__(self, __o: object) -> bool:
        return all(
            [
                self.x == __o.x,
                self.y == __o.y,
            ]
        )

    def __str__(self) -> str:
        return f"X {self.x} Y {self.y}"

    def __repr__(self) -> str:
        return str(self)


class Directions(Enum):
    up: Location = Location(-1, 0)
    down: Location = Location(1, 0)
    left: Location = Location(0, -1)
    right: Location = Location(0, 1)


class GameModel:
    def __init__(self, model: str = ".") -> None:
        self.model: str = model

    def __str__(self) -> str:
        return self.model

    def __repr__(self) -> str:
        return str(self)


class GameObject:
    def __init__(
        self,
        gm: "GameManager",
        name: str = "",
        loc: Location = Location(),
        model: GameModel = GameModel(),
    ) -> None:
        self.gm: GameManager = gm
        self.name: str = name
        self.loc: Location = loc
        self.model: GameModel = model
        self.destroy: bool = bool()

    def update(self) -> None:
        pass

    def collide(self, other: Type["GameObject"]) -> None:
        pass

    def destruct(self) -> None:
        self.destroy = True

    def __str__(self) -> str:
        return f"{self.name} [{self.model}] -> {self.loc}"

    def __repr__(self) -> str:
        return str(self)


class Player(GameObject):
    def __init__(
        self,
        gm: "GameManager",
        name: str = "Player",
        loc: Location = Location(),
        model: GameModel = GameModel("A"),
    ) -> None:
        super().__init__(gm, name, loc, model)
        self.hits: List[Location] = list()

    def update(self) -> None:
        cmd, *param = input().split()
        getattr(self, cmd)(*param)
        super().update()

    def move(self, direction: str, distance: str) -> None:
        direct: Location = Directions[direction].value
        for _ in range(int(distance)):
            new_loc = self.loc + direct
            if self.gm.location_valid(new_loc):
                self.loc = new_loc
            if self.gm.collide(self):
                self.loc -= direct

    def shoot(self, direction: str) -> None:
        self.gm.objects.append(
            Projectile(
                self.gm, self, direction=Directions[direction].value, loc=self.loc
            )
        )


class Projectile(GameObject):
    def __init__(
        self,
        gm: "GameManager",
        owner: Type[GameObject],
        direction: Location,
        name: str = "Projectile",
        loc: Location = Location(),
        model: GameModel = GameModel("*"),
    ) -> None:
        super().__init__(gm, name, loc, model)
        self.owner: Type[GameObject] = owner
        self.direction: Location = direction

    def update(self) -> None:
        super().update()
        while self.gm.location_valid(self.loc):
            self.loc += self.direction
            other: Type[GameObject] = self.gm.collide(self)
            if type(other) == Target:
                self.owner.hits.append(self.loc)
                other.collide(self)
                self.destruct()
                return
        self.destruct()


class Target(GameObject):
    def __init__(
        self,
        gm: "GameManager",
        name: str = "Target",
        loc: Location = Location(),
        model: GameModel = GameModel("x"),
    ) -> None:
        super().__init__(gm, name, loc, model)

    def collide(self, other: Type["GameObject"]) -> None:
        super().collide(other)
        if type(other) == Projectile:
            self.destruct()


objects_dict: Dict[str, Type[GameObject]] = {
    ".": GameObject,
    "A": Player,
    "*": Projectile,
    "x": Target,
}


class GameManager:
    def __init__(self) -> None:
        self.area: int = 5
        self.objects: List[Type[GameObject]] = list()
        for x in range(5):
            col: List[str] = input().split()
            for y in range(5):
                if col[y] != ".":
                    self.objects.append(objects_dict[col[y]](self, loc=Location(x, y)))

    def play(self) -> None:
        if DEBUG:
            print(self)
        for obj in self.objects:
            obj.update()
        if DEBUG:
            print(self)
        for obj in filter(lambda o: o.destroy, self.objects):
            self.objects.remove(obj)

    def location_valid(self, loc: Location) -> bool:
        return all(
            [
                loc.x in range(self.area),
                loc.y in range(self.area),
            ]
        )

    def collide(self, collider: Type[GameObject]) -> Type[GameObject]:
        colliders: List[Type[GameObject]] = list(
            filter(
                lambda x: not x is collider and x.loc == collider.loc,
                self.objects,
            )
        )
        return colliders[0] if colliders else None

    def blank_grid(self) -> List[List[str]]:
        return [["." for y in range(self.area)] for x in range(self.area)]

    def draw_grid(self) -> str:
        grid: List[List[str]] = self.blank_grid()
        for obj in self.objects:
            if self.location_valid(obj.loc):
                grid[obj.loc.x][obj.loc.y] = obj.model.model
        return "\n".join([" ".join(row) for row in grid])

    def __str__(self) -> str:
        return "\n".join(
            [
                self.draw_grid(),
                # "\n".join(map(str, self.objects)),
                "",
            ]
        )

    def __repr__(self) -> str:
        return str(self)


def solution() -> None:
    gm: GameManager = GameManager()

    targets_init = list(filter(lambda o: type(o) == Target, gm.objects))
    player: Player = list(filter(lambda o: type(o) == Player, gm.objects))[0]

    for _ in range(int(input())):
        gm.play()

    targets_left = list(filter(lambda o: type(o) == Target, gm.objects))

    if targets_left:
        print(f"Training not completed! {len(targets_left)} targets left.")
    else:
        print(f"Training completed! All {len(targets_init)} targets hit.")
    for hit in player.hits:
        print(f"[{hit.x}, {hit.y}]")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
