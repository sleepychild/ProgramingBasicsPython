from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Don Quixote&The Great Gatsby&Moby Dick',
        'Add Book | Ulysses',
        'Take Book | Don Quixote',
        "Insert Book | Alice's Adventures in Wonderland",
        'Done',
    ),
    (
        'Anna Karenina&Heart of Darkness&Catch-22&The Stranger',
        'Add Book | Catch-22',
        'Swap Books | Anna Karenina | Catch-22',
        'Take Book | David Copperfield',
        'Done',
    ),
    (
        'War and Peace&Hamlet&Ulysses&Madame Bovary',
        'Check Book | 2',
        'Swap Books | Don Quixote | Ulysses',
        'Done',
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

    def __init__(self) -> None:
        pass

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:

    def __init__(self) -> None:
        self.books: List[str] = input().split('&')

    def __str__(self) -> str:
        return ', '.join(self.books)

    def run(self) -> None:
        while True:
            cmd: str = input()
            if cmd == 'Done':
                print(self)
                break
            else:
                option, *parameters = cmd.split(' | ')
                if DEBUG: print(option, parameters)
                if option == "Add Book" and parameters[0] not in self.books:
                    self.books.insert(FIRST, parameters[0])
                elif option == "Take Book" and parameters[0] in self.books:
                    self.books.remove(parameters[0])
                elif option == "Swap Books" and parameters[0] in self.books and parameters[1] in self.books:
                    book_a_index: int = self.books.index(parameters[0])
                    book_b_index: int = self.books.index(parameters[1])
                    self.books[book_a_index], self.books[book_b_index] = self.books[book_b_index], self.books[book_a_index]
                elif option == "Insert Book" and parameters[0] not in self.books:
                    self.books.append(parameters[0])
                elif option == "Check Book":
                    book_index: int = int(parameters[0])
                    if book_index in range(len(self.books)):
                        print(self.books[book_index])

def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        print('=== NEW RUN ===')
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
