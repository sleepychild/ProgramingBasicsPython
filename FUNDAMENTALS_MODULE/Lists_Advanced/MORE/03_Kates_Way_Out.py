from typing import List, Tuple, Generator, Callable, Union
from copy import deepcopy
from enum import Enum

test_runs: Tuple[Tuple[str]] = (
    # (
    #     '4',
    #     '######',
    #     '##  k#',
    #     '## ###',
    #     '## ###',
    # ),
    # (
    #     '5',
    #     '######',
    #     '##  k#',
    #     '## ###',
    #     '######',
    #     '## ###',
    # ),(
    #     '6',
    #     '######',
    #     '##  k ',
    #     '## ###',
    #     '#     ',
    #     '## ###',
    #     '## ###',
    # ),(
    #     '3',
    #     '######',
    #     '#####k',
    #     '######',
    # ),
    (
        '3',
        '# #',
        ' k ',
        '# #',
    ),
    # (
    #     '1',
    #     'k',
    # ),
)


class Directions(Enum):
    UP: Tuple[int] = (0, -1,)
    DOWN: Tuple[int] = (0, 1,)
    LEFT: Tuple[int] = (-1, 0,)
    RIGHT: Tuple[int] = (1, 0,)


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __add__(self, other: Union['Position', Tuple]) -> 'Position':
        if type(other) == tuple:
            return Position(self.x + other[0], self.y + other[1])
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Position') -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f'{self.x} : {self.y}'


class PlayerPath:
    def __init__(self, start: Position) -> None:
        self.moving: bool = True
        self.at_exit: bool = False
        self.path: List[Position] = list()
        self.path.append(start)

    def __len__(self) -> int:
        return len(self.path)

    def __gt__(self, other: 'PlayerPath') -> bool:
        return len(self.path) > len(other.path)

    def current_position(self) -> Position:
        return self.path[-1]


class Player:
    def __init__(self, start: Position) -> None:
        self.paths: List[PlayerPath] = list()
        self.paths.append(PlayerPath(start))

    def result(self) -> None:
        try:
            print(f'Kate got out in { len(sorted(list(filter(lambda p: p.at_exit, self.paths)),reverse=True)[0]) } moves')
        except IndexError as _:
            print('Kate cannot get out')

    def fork(self, fork: List[Position], path: PlayerPath) -> None:
        for f in fork:
            new_path: PlayerPath = deepcopy(path)
            new_path.path.append(f)
            self.paths.append(new_path)

    def moving(self) -> bool:
        return True in [p.moving for p in self.paths]


class MazeClass:
    def __init__(self, maze: List[List[bool]]) -> None:
        self.maze: List[List[bool]] = maze

    def traversible(self, position: Position) -> bool:
        return self.maze[position.y][position.x]

    def get_traversible_positions(self, position: Position) -> List[Position]:
        return list(filter(self.traversible, [position + d.value for d in Directions]))


class Control:
    def __init__(self, maze: MazeClass, player: Player) -> None:
        self.maze: MazeClass = maze
        self.player: Player = player

    def run(self):
        while self.player.moving():
            self.move_player()

        self.player.result()

    def move_player(self) -> None:
        for player_path in self.player.paths:
            player_current_position: Position = player_path.current_position()

            try:
                traversable_positions = self.maze.get_traversible_positions(
                    player_current_position)
            except IndexError as _:
                player_path.moving = False
                player_path.at_exit = True
                continue

            next_positions: List[Position] = list(
                filter(lambda tp: not tp in player_path.path, traversable_positions))

            print("======================")
            print(player_path.moving, player_path.at_exit,
                  player_path.path[-1])
            for pp in player_path.path:
                print('pp: ', pp, end=", ")
            print()
            for tp in traversable_positions:
                print('tp: ', tp, end=", ")
            print()
            for np in next_positions:
                print('np: ', np, end=", ")

            npl: int = len(next_positions)
            if npl == 0:
                player_path.moving = False
            elif npl == 1:
                player_path.path.append(next_positions[0])
            else:
                self.player.fork(next_positions[1:], player_path)
                player_path.path.append(next_positions[0])

            print("\n", player_path.moving,
                  player_path.at_exit, player_path.path[-1])
            print("======================")

    def __str__(self) -> str:
        maze_str: str = str()
        for r, row in enumerate(self.maze):
            for c, col in enumerate(row):
                maze_str += 'K' if self.player.location_check(
                    c, r) else ' ' if col else '#'
            maze_str += '\n'
        return maze_str

    @staticmethod
    def row_from_string(row_string: str, non_traversible_str: str) -> List[bool]:
        return [l != non_traversible_str for l in row_string]

    @classmethod
    def FromInput(cls, non_traversible_str: str, player_str: str) -> 'MazeClass':
        maze: List[List[bool]] = list()
        for i in range(int(input())):
            row_string: str = input()
            maze.append(cls.row_from_string(row_string, non_traversible_str))
            if player_str in row_string:
                player_position: Position = Position(
                    row_string.index(player_str), i)
        return cls(MazeClass(maze), Player(player_position))


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    ctrl = Control.FromInput('#', 'k')
    ctrl.run()


for test_run in test_runs:
    input: Callable[[], str] = get_run_generator(test_run)
    solution()

# solution()
