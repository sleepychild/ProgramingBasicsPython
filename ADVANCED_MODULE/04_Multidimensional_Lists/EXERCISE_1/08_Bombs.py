from typing import Generator, Callable, Tuple, List

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "4",
        "8 3 2 5",
        "6 4 7 9",
        "9 9 3 6",
        "6 8 1 2",
        "1,2 2,1 2,0",
    ),
    (
        "3",
        "7 8 4",
        "3 1 5",
        "6 4 9",
        "0,2 1,0 2,2",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Grid:
    def __init__(self, grid_size: int) -> None:
        self.grid_size: int = grid_size
        self.grid: List[List[int]] = [
            list(map(int, input().split())) for _ in range(self.grid_size)
        ]

    def valid(self, row: int, col: int) -> bool:
        return all(
            [
                row in range(self.grid_size),
                col in range(self.grid_size),
            ]
        )

    def alive(self, row: int, col: int) -> bool:
        return self.grid[row][col] > 0

    def detonate(self, row: int, col: int) -> None:
        if not (self.valid(row, col) and self.alive(row, col)):
            return
        dmg: int = self.grid[row][col]
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if self.valid(r, c) and self.alive(r, c):
                    self.grid[r][c] -= dmg

    def alive_count_and_sum(self) -> Tuple[int, int]:
        a_count: int = int()
        a_sum: int = int()
        for row in self.grid:
            for col in row:
                if col > 0:
                    a_count += 1
                    a_sum += col
        return a_count, a_sum

    def __str__(self) -> str:
        return "\n".join([f"{' '.join(map(str, row))}" for row in self.grid])

    def __repr__(self) -> str:
        return str(self)


def solution() -> None:
    grid: Grid = Grid(int(input()))

    for bomb in [[int(c) for c in b.split(",")] for b in input().split()]:
        grid.detonate(*bomb)

    alive_count: int
    alive_sum: int

    alive_count, alive_sum = grid.alive_count_and_sum()

    print(f"Alive cells: {alive_count}\nSum: {alive_sum}")
    print(grid)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
