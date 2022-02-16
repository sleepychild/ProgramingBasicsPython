from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        '. . - - -',
        '. . - - -',
        '- - - - -',
        '- - - . .',
        '- - - . .',
    ),
    (
        '6',
        '. . - . - .',
        '- . . . . .',
        '- . - - - -',
        '- . . - - -',
        '- . . . . -',
        '- - - . . -',
    ),
    (
        '4',
        '- . - . . -',
        '. - . . - .',
        '. - - - - -',
        '- - - . - -',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

FIRST: int = 0
LAST: int = -1

class Directions(Enum):
    UP: Tuple[int] = (-1, 0,)
    RIGHT: Tuple[int] = (0, 1,)
    DOWN: Tuple[int] = (1, 0,)
    LEFT: Tuple[int] = (0, -1,)


class Tile:

    def __init__(self, row: int = 0, col: int = 0, traversible: bool = False, end: bool = False) -> None:
        self.row: int = row
        self.col: int = col
        self.traversible: bool = traversible
        self.end: bool = end

    def neighbours(self) -> Tuple[Tuple[int]]:
        return tuple([self + direction.value for direction in Directions])

    def __add__(self, other: Union['Tile', Tuple]) -> Tuple:
        if type(other) == tuple:
            return (self.row + other[0], self.col + other[1],)
        return (self.row + other.col, self.row + other.row,)

    def __str__(self) -> str:
        return f'|{self.row}:{self.col}/{"T" if self.traversible else "_"}{"E" if self.end else "_"}|'


class Traversal:

    def __init__(self) -> None:
        self.path: List[Tile] = list()

    def active(self) -> bool:
        for tile in self.path:
            if tile.end:
                return True
        return False

    def get_ends(self) -> List[Tile]:
        return [ tile for tile in self.path if tile.end ]

    def __contains__(self, tile: Tile) -> bool:
        if tile in self.path:
            return True
        return False
    
    def __str__(self) -> str:
        return ' => '.join([str(p) for p in self.path])

class Traversals:

    def __init__(self):
        self.list: List[Traversal] = list()

    def active(self) -> bool:
        for traversal in self.list:
            if traversal.active():
                return True
        return False

    def __contains__(self, tile: Tile) -> bool:
        for traversal in self.list:
            if tile in traversal:
                return True
        return False


class GridClass:

    def __init__(self, grid: List[List[Tile]]) -> None:
        self.grid: List[List[Tile]] = grid
        self.range_row: Tuple[int] = tuple(range(0, len(self.grid)))
        self.range_col: Tuple[int] = tuple(range(0, len(self.grid[0])))

    def traversible(self, tile: Union[Tile, Tuple]) -> bool:
        if type(tile) == tuple and tile[0] in self.range_row and tile[1] in self.range_col:
            return self.grid[tile[0]][tile[1]].traversible
        elif type(tile) == Tile and tile.row in self.range_row and tile.col in self.range_col:
            return self.grid[tile.row][tile.col].traversible
        else:
            return False

    def tile_gen(self) -> Generator[Tile, None, None]:
        for row in self.range_row:
            for col in self.range_col:
                yield self.grid[row][col]

    def __str__(self) -> str:
        string_out: str = str()
        for row in self.grid:
            string_out += f"{' '.join([ str(e) for e in row ])}\n"
        string_out += f"rows: {self.range_row} | cols: {self.range_col}"
        return string_out

    @classmethod
    def FromInput(cls) -> 'GridClass':
        grid: List[List[Tile]] = list()
        for row_i in range(int(input())):
            grid_row: List[Tile] = list()
            for col_i, col_v in enumerate([ c == '.' for c in input().split(' ') ]):
                grid_row.append(Tile(row_i, col_i, col_v))
            grid.append(grid_row)
        return cls(grid)


class ControlClass:

    def __init__(self) -> None:
        self.map: GridClass = GridClass.FromInput()
        self.traversals: Traversals = Traversals()

    def run(self) -> None:
        if DEBUG: print(self)
        tg: Generator[Tile, None, None] = self.map.tile_gen()
        while True:
            try:
                gt: Tile = next(tg)
            except StopIteration as e:
                if DEBUG: print(e)
                return
            else:
                if DEBUG: print(gt, gt.traversible and gt not in self.traversals, gt.neighbours())
                if gt.traversible and gt not in self.traversals:
                    gt.end = True
                    self.traversals.list.append(Traversal())
                    self.traversals.list[LAST].path.append(gt)
                    while self.traversals.list[LAST].active():
                        for end_tile in self.traversals.list[LAST].get_ends():
                            end_tile.end = False
                            for neighbour in end_tile.neighbours():
                                if self.map.traversible(neighbour) and self.map.grid[neighbour[0]][neighbour[1]] not in self.traversals:
                                    self.traversals.list[LAST].path.append(self.map.grid[neighbour[0]][neighbour[1]])
                                    self.traversals.list[LAST].path[LAST].end = True
                        if DEBUG: print(self)


            
    def __str__(self) -> str:
        return_str: str = str()
        return_str += str(self.map)
        return_str += '\n'
        return_str += '\n'.join([ str(t) for t in self.traversals.list ])
        return return_str


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()
    try:
        print(max([ len(t.path) for t in ctrl.traversals.list ]))
    except ValueError as _:
        print(0)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
