from typing import List, Tuple, Generator, Callable, Union
from copy import deepcopy
from enum import Enum

DEBUG: bool = True

test_runs: Tuple[Tuple[str]] = (
    (
        '4',
        '######',
        '##  k#',
        '## ###',
        '## ###',
    ),
    (
        '5',
        '######',
        '##  k#',
        '## ###',
        '######',
        '## ###',
    ),
    (
        '6',
        '######',
        '##  k ',
        '## ###',
        '#     ',
        '## ###',
        '## ###',
    ),
    (
        '3',
        '######',
        '     k',
        '######',
    ),
    (
        '3',
        '# #',
        ' k ',
        '# #',
    ),
    (
        '1',
        'k',
    ),
    (
        '1',
        ' k ',
    ),
    (
        '3',
        ' ',
        'k',
        ' ',
    ),
    (
        '10',
        '###########',
        '#         #',
        '#         #',
        '#         #',
        '#         #',
        '#         #',
        '#         #',
        '# #####   #',
        '#       k #',
        '# #########',
    ),
    (
        '5',
        '## ##',
        '#   #',
        '# # #',
        '# k #',
        '#####',
    ),
    (
        '6',
        '##########',
        '#        #',
        '#        #',
        '# ####   #',
        '#      k #',
        '# ########',
    ),
)


class Directions(Enum):
    UP: Tuple[int] = (0, -1,)
    RIGHT: Tuple[int] = (1, 0,)
    DOWN: Tuple[int] = (0, 1,)
    LEFT: Tuple[int] = (-1, 0,)

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

    def __int__(self) -> int:
        return min(self.x, self.y)

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

    def __str__(self) -> str:
        return f'moving: {self.moving} at_exit: {self.at_exit} position: {self.current_position()} length: {len(self.path)}'

    def current_position(self) -> Position:
        return self.path[-1]


class Player:
    def __init__(self, start: Position) -> None:
        self.start: Position = start
        self.paths: List[PlayerPath] = list()
        self.paths.append(PlayerPath(start))

    def result(self) -> None:
        try:
            _: PlayerPath = list(filter(lambda p: p.at_exit, self.paths))[0]
            print(f'Kate got out in { len(self.get_final_path()) - 1 } moves')
        except IndexError as _:
            print('Kate cannot get out')
        

    def get_final_path(self) -> int:
        final_exit_paths: List[PlayerPath] = list()
        exit_paths: List[PlayerPath] = list(filter(lambda p: p.at_exit, self.paths))
        dead_paths: List[PlayerPath] = list(filter(lambda p: not p.at_exit, self.paths))

        for ext_pth in exit_paths:
            for ep_pos in ext_pth.path:
                for dir_pos in [ ep_pos + d.value for d in  Directions ]:
                    for de_pth in dead_paths:
                        if dir_pos == de_pth.current_position():
                            ext_index: int = ext_pth.path.index(ep_pos)
                            de_index: int = de_pth.path.index(dir_pos)
                            if ext_index - de_index > 1:
                                if DEBUG:
                                    print([str(p) for p in ext_pth.path])
                                    print([str(p) for p in de_pth.path])
                                    print([str(p) for p in de_pth.path[:de_index+1] + ext_pth.path[ext_index:]])
                                    fep: PlayerPath = PlayerPath(self.start)
                                    fep.path = de_pth.path[:de_index+1] + ext_pth.path[ext_index:]
                                    final_exit_paths.append(fep)

        if DEBUG:
            for pth in final_exit_paths:
                print(pth, '\n', [str(p) for p in pth.path])

        if len(final_exit_paths) > 0:
            return sorted(final_exit_paths, reverse=True)[0]
        else:
            return sorted(exit_paths, reverse=True)[0]

    def location_check(self, loc: Position) -> bool:
        return loc in [ p.current_position() for p in self.paths ]
        

    def not_visited(self, traversible_position: Position) -> bool:
        all_positions: List[Position] = list()
        for path in self.paths:
            all_positions += path.path
        return traversible_position not in all_positions

    def fork(self, fork: List[Position], path: PlayerPath) -> List[PlayerPath]:
        new_paths: List[PlayerPath] = list()
        for f in fork:
            new_path: PlayerPath = deepcopy(path)
            new_path.path.append(f)
            new_paths.append(new_path)
            self.paths.append(new_path)
            if DEBUG: print(f'NEW_PATH: {new_path}')
        return new_paths

    def moving(self) -> bool:
        return True in [p.moving for p in self.paths]


class MazeClass:
    def __init__(self, maze: List[List[bool]]) -> None:
        self.maze: List[List[bool]] = maze

        self.range_x: range = range(len(self.maze[0]))
        self.range_y: range = range(len(self.maze))

        self.r_x: Tuple[int] = (0, len(self.maze[0]) - 1,)
        self.r_y: Tuple[int] = (0, len(self.maze) - 1,)

        self.tr_x: Tuple[int] = (-1, len(self.maze[0]),)
        self.tr_y: Tuple[int] = (-1, len(self.maze),)

    def traversible(self, position: Position) -> bool:
        if position.x in self.tr_x or position.y in self.tr_y:
            return True
        else:
            try:
                return self.maze[position.y][position.x]
            except IndexError as _:
                return False

    def get_traversible_positions(self, position: Position) -> List[Position]:
        return list(filter(self.traversible, [position + d.value for d in Directions]))


class Control:
    def __init__(self, maze: MazeClass, player: Player) -> None:
        self.maze: MazeClass = maze
        self.player: Player = player
        if not DEBUG:
            if self.maze.range_x == range(1) == self.maze.range_y:
                print(f'Kate got out in 1 moves')
                exit(0)

    def run(self):
        while self.player.moving():
            self.move_player()

        self.player.result()
        if DEBUG:
            print(f'player paths {len(self.player.paths)}')
            print('\nDead Ends:')
            for pth in sorted([ path for path in self.player.paths if not path.at_exit ]):
                print(pth, '\n', [str(p) for p in pth.path])
            print('\nExits:')
            for pth in sorted([ path for path in self.player.paths if path.at_exit ]):
                print(pth, '\n', [str(p) for p in pth.path])
            print('\nAll:')
            for pth in sorted(self.player.paths):
                print([str(p) for p in pth.path])
            
    def move_player(self) -> None:
        for pi, player_path in enumerate(self.player.paths):

            if DEBUG: print(f"\n========={pi}===========")
            if DEBUG: print(player_path)

            player_current_position: Position = player_path.current_position()
            traversable_positions = self.maze.get_traversible_positions(player_current_position)
            next_positions: List[Position] = list(filter(self.player.not_visited, traversable_positions))
            npl: int = len(next_positions)

            if DEBUG: 
                for pp in player_path.path:
                    print('pp: ', pp, end=", ")
                print()

                for tp in traversable_positions:
                    print('tp: ', tp, end=", ")
                print()

                for np in next_positions:
                    print('np: ', np, end=", ")
                print()

            if self.check_exit(player_current_position):
                player_path.at_exit = True
                player_path.moving = False
            
            if npl == 0:
                player_path.moving = False
            elif npl == 1 and player_path.moving:
                player_path.path.append(next_positions[0])
            
            if npl > 1 and not self.check_exit(player_path.current_position()):
                for npth in self.player.fork(next_positions[1:], player_path):
                    if self.check_exit(npth.current_position()):
                        npth.at_exit = True
                        npth.moving = False
                player_path.path.append(next_positions[0])

            if self.check_exit(player_path.current_position()):
                player_path.at_exit = True
                player_path.moving = False

            if DEBUG: print(player_path)

            if DEBUG: print(f"========={pi}===========\n")
            if DEBUG: print(self)


    def check_exit(self, position: Position) -> bool:
        if position.x in self.maze.tr_x or position.y in self.maze.tr_y:
            return True
        else:
            return False

    def __str__(self) -> str:
        maze_str: str = str()
        for r, row in enumerate(self.maze.maze):
            for c, col in enumerate(row):
                maze_str += 'K' if self.player.location_check(Position(c, r)) else ' ' if col else '#'
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
    if DEBUG: print(ctrl)
    ctrl.run()

if DEBUG: 
    for test_run in test_runs:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
