from typing import ClassVar, Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Beer 2.20 100',
        'IceTea 1.50 50',
        'NukaCola 3.30 80',
        'Water 1.00 500',
        'buy',
    ),
    (
        'Beer 2.40 350',
        'Water 1.25 200',
        'IceTea 5.20 100',
        'Beer 1.20 200',
        'IceTea 0.50 120',
        'buy',
    ),
    (
        'CesarSalad 10.20 25',
        'SuperEnergy 0.80 400',
        'Beer 1.35 350',
        'IceCream 1.50 25',
        'buy',
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
        self.order: Dict[str, Dict[str, Union[float, int]]] = dict()

    def run(self) -> None:
        while True:
            line_in: str = input()
            if line_in == 'buy':
                break
            else:
                n, p, q = line_in.split()
                name: str = n
                price: float = float(p)
                quantity: int = int(q)
                if name not in self.order:
                    self.order[name] = {
                        "price": price,
                        "quantity": quantity
                    }
                else:
                    self.order[name]["price"] = price
                    self.order[name]["quantity"] += quantity
        for k, v in self.order.items():
            print(f'{k} -> { v["quantity"] * v["price"] :.2f}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
