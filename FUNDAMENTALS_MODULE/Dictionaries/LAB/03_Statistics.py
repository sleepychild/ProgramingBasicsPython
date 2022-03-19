from typing import Tuple, Generator, Callable, Dict
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'bread: 4',
        'cheese: 2',
        'ham: 1',
        'bread: 1',
        'statistics',
    ),
    (
        'eggs: 10',
        'bread: 6',
        'cheese: 8',
        'milk: 7',
        'statistics',
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

    def run(self) -> None:
        stocks: Dict = dict()
        while True:
            line_in: str = input()
            if line_in == 'statistics':
                break
            else:
                k, v = line_in.split(': ')
                try:
                    stocks[k] += int(v)
                except KeyError as e:
                    stocks[k] = int(v)
        print('Products in stock:')
        for s_k, s_v in stocks.items():
            print(f'- {s_k}: {s_v}')
        print(f'Total Products: {len(stocks.keys())}')
        print(f"Total Quantity: {sum(stocks.values())}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
