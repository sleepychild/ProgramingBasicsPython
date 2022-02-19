from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '1 1 2 2 3 3 4 4 5 5',
        '1 0',
        '-1 0',
        '1 0',
        '1 0',
        '1 0',
        'end',
    ),
    (
        'a 2 4 a 2 4',
        '0 3',
        '0 2',
        '0 1',
        '0 1',
        'end',
    ),
    (
        'a 2 4 a 2 4',
        '4 0',
        '0 2',
        '0 1',
        '0 1',
        'end',
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


class Base:

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:
    def __init__(self) -> None:
        self.board: List[str] = input().split(' ')
        self.moves: int = int()

    def run(self) -> None:
        while len(self.board) > 0:
            if DEBUG:
                print(self.board)
            cmd: str = input()
            if DEBUG:
                print(cmd)
            if cmd == 'end':
                break
            else:
                self.moves += 1
                a, b = [int(p) for p in cmd.split(' ')]
                if DEBUG:
                    print(a, b)
                cbr: range = range(len(self.board))
                if a != b and a in cbr and b in cbr:
                    if self.board[a] == self.board[b]:
                        hit: str = self.board[a]
                        print(
                            f"Congrats! You have found matching elements - {hit}!")
                        self.board.remove(hit)
                        self.board.remove(hit)
                    else:
                        print("Try again!")
                else:
                    print('Invalid input! Adding additional elements to the board')
                    pos: int = len(self.board) // 2
                    self.board.insert(pos, f'-{self.moves}a')
                    self.board.insert(pos, f'-{self.moves}a')
        if len(self.board) > 0:
            print('Sorry you lose :(')
            print(' '.join(self.board))
        else:
            print(f"You have won in {self.moves} turns!")

def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
