from typing import Generator, Callable, Tuple, List, Dict, ClassVar, Type
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "5",
        "0K0K0",
        "K000K",
        "00K00",
        "K000K",
        "0K0K0",
    ),
    (
        "2",
        "KK",
        "KK",
    ),
    (
        "8",
        "0K0KKK00",
        "0K00KKKK",
        "00K0000K",
        "KKKKKK0K",
        "K0K0000K",
        "KK00000K",
        "00K0K000",
        "000K00KK",
    ),
    (
        "3",
        "K0K",
        "000",
        "0K0",
    ),
    (
        "5",
        "KKKKK",
        "K000K",
        "K000K",
        "K000K",
        "KKKKK",
    ),
    (
        "10",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
        "KKKKKKKKKK",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class ChessPiece:
    model: ClassVar[str] = "0"

    class AllowedMoves(Enum):
        pass

    class AllowedAttacks(Enum):
        pass

    def __init__(self, parent: "ChessBoard", x: int, y: int) -> None:
        self.parent: "ChessBoard" = parent
        self.x: int = x
        self.y: int = y

    def valid_moves(self) -> List[Tuple[int, int]]:
        return self._valid(self.AllowedMoves)

    def valid_attacks(self) -> List[Tuple[int, int]]:
        return self._valid(self.AllowedAttacks)

    def _valid(self, allowed: Type[Enum]) -> List[Tuple[int, int]]:
        val_mov: List[Tuple[int, int]] = list()
        for a in allowed:
            next_x: int = self.x + a.value[0]
            next_y: int = self.y + a.value[1]
            if self.parent.valid(next_x, next_y):
                val_mov.append(
                    (
                        next_x,
                        next_y,
                    )
                )
        return val_mov

    def targets(self) -> List[Tuple[int, int]]:
        return list(
            filter(
                lambda x: self.parent.grid[x[0]][x[1]] != ChessPiece.model,
                self.valid_attacks(),
            )
        )

    def __str__(self) -> str:
        return f"{self.model} -> x:{self.x} y:{self.y} trg:{self.targets()}"

    def __repr__(self) -> str:
        return str(self)


class Knight(ChessPiece):
    model: ClassVar[str] = "K"

    class AllowedMoves(Enum):
        UL: Tuple[int, int] = (
            -1,
            -2,
        )
        LU: Tuple[int, int] = (
            -2,
            -1,
        )
        LD: Tuple[int, int] = (
            -2,
            1,
        )
        DL: Tuple[int, int] = (
            -1,
            2,
        )
        UR: Tuple[int, int] = (
            1,
            2,
        )
        RU: Tuple[int, int] = (
            2,
            1,
        )
        RD: Tuple[int, int] = (
            2,
            -1,
        )
        DR: Tuple[int, int] = (
            1,
            -2,
        )

    class AllowedAttacks(Enum):
        UL: Tuple[int, int] = (
            -1,
            -2,
        )
        LU: Tuple[int, int] = (
            -2,
            -1,
        )
        LD: Tuple[int, int] = (
            -2,
            1,
        )
        DL: Tuple[int, int] = (
            -1,
            2,
        )
        UR: Tuple[int, int] = (
            1,
            2,
        )
        RU: Tuple[int, int] = (
            2,
            1,
        )
        RD: Tuple[int, int] = (
            2,
            -1,
        )
        DR: Tuple[int, int] = (
            1,
            -2,
        )


class ChessBoard:
    class Pieces(Enum):
        KNIGHT: Type[ChessPiece] = Knight

    def __init__(self, size: int, grid: List[List[str]]) -> None:
        self.size: int = size
        self.grid: List[List[str]] = grid

    def remove(self, piece: Type[ChessPiece]) -> None:
        self.grid[piece.x][piece.y] = ChessPiece.model

    def valid(self, x: int, y: int) -> bool:
        return all(
            [
                x in range(self.size),
                y in range(self.size),
            ]
        )

    def get_chess_pieces(self) -> List[Dict]:
        chess_pieces: List[Type[ChessPiece]] = list()
        for Piece in self.Pieces:
            for row in range(self.size):
                for col in range(self.size):
                    if self.grid[row][col] == Piece.value.model:
                        chess_pieces.append(Piece.value(self, row, col))
        return chess_pieces

    def __str__(self) -> str:
        grid_str: str = "\n".join([f"{''.join(row)}" for row in self.grid])
        pieces_str: str = "\n".join([str(pcs) for pcs in self.get_chess_pieces()])
        return f"{grid_str}\n{pieces_str}"

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def from_input(cls) -> "ChessBoard":
        size: int = int(input())
        grid: List[List[str]] = list()

        for _ in range(size):
            grid.append(list(input()))

        return cls(size, grid)


def solution() -> None:
    board: ChessBoard = ChessBoard.from_input()
    removed_pieces: int = int()

    while True:
        try:
            acctionable: Type[ChessPiece] = sorted(
                filter(lambda x: x.targets(), board.get_chess_pieces()),
                key=lambda x: len(x.targets()),
                reverse=True,
            )[0]
        except IndexError as _:
            print(removed_pieces)
            break
        else:
            board.remove(acctionable)
            removed_pieces += 1


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
