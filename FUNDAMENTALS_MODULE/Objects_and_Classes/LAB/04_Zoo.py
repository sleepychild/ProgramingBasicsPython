from typing import ClassVar, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Great Zoo',
        '5',
        'mammal lion',
        'mammal bear',
        'fish salmon',
        'bird owl',
        'mammal tiger',
        'mammal',
    ),
    (
        'Blah',
        '1',
        'mammal bear',
        'mammal',
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

class Species:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.animals: List[str] = list()

    def add_animal(self, name: str) -> None:
        self.animals.append(name)

    def __str__(self) -> str:
        return ", ".join(self.animals)

class Zoo:
    __animals: int = int()

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.mammal: Species = Species('Mammals')
        self.fish: Species = Species('Fishes')
        self.bird: Species = Species('Birds')

    def add_animal(self, species: str, name: str) -> None:
        self.__getattribute__(species).add_animal(name)
        self.__animals += 1

    def get_info(self, species: str) -> str:
        spcs: Species = self.__getattribute__(species)
        return f'{spcs.name} in {self.name}: {str(spcs)}\nTotal animals: {self.__animals}'


class Base:

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:

    def run(self) -> None:
        z: Zoo = Zoo(input())
        for _ in range(int(input())):
            z.add_animal(*input().split(' '))
        print(z.get_info(input()))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
