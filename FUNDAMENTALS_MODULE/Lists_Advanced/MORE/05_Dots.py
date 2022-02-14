from typing import List, Tuple, Generator, Callable

DEBUG: bool = True

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

class GridClass:
    
    def __init__(self, grid: List[List[bool]]) -> None:
        self.grid: List[List[bool]] = grid
        self.range_row: Tuple[int] = tuple(range(0, len(self.grid)))
        self.range_col: Tuple[int] = tuple(range(0, len(self.grid[0])))

    def __str__(self) -> str:
        string_out: str = str()
        for row in self.grid:
            string_out += f"{' '.join([ '.' if e else '-' for e in row])}\n"
        string_out += f"rows: {self.range_row} | cols: {self.range_col}"
        return string_out

    @staticmethod
    def row_from_string(row_string: str) -> List[bool]:
        return [ l == '.' for l in row_string.split(' ')]

    @classmethod
    def FromInput(cls) -> 'GridClass':
        grid: List[List[int]] = list()
        for _ in range(int(input())):
            grid.append(cls.row_from_string(input()))
        return cls(grid)

def solution():
    grid: GridClass = GridClass.FromInput()
    if DEBUG: print(grid)

if DEBUG: 
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
