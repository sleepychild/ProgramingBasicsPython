from typing import List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000',
    ),
    (
        'cat 10|potion 30|orc 10|chest 10|snake 25|chest 110',
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


class Player:
    def __init__(self) -> None:
        self.bitcoins: int = 0
        self.hp: int = 100
        self._MAX_HP: int = 100
        self.loc: int = 0

    def isalive(self) -> bool:
        return self.hp > 0

    def heal(self, amount: int) -> None:
        init_health: int = self.hp
        self.hp = min(self._MAX_HP, self.hp + amount)
        print(f'You healed for {self.hp - init_health} hp.')
        print(f'Current health: {self.hp} hp.')

    def loot(self, amount: int) -> None:
        self.bitcoins += amount
        print(f'You found {amount} bitcoins.')

    def fight(self, enemy: str, dmg: int) -> bool:
        self.hp -= dmg
        if self.isalive():
            print(f'You slayed {enemy}.')
            return True
        else:
            print(f'You died! Killed by {enemy}.')
            return False


class Room:
    def __init__(self, num: int, act: str, val: int) -> None:
        self.num: int = num
        self.act: str = act
        self.val: int = val

    def __str__(self) -> str:
        return f'{self.num}: {self.act} for {self.val}'

class Base:
    def __init__(self, rooms: List[Room]) -> None:
        self.rooms: List[Room] = rooms

    def __str__(self) -> None:
        return '\n'.join([str(r) for r in self.rooms])

    @classmethod
    def FromInput(cls) -> 'Base':
        rooms: List[Room] = list()
        r_num: int = 1
        for r in input().split('|'):
            r_act, r_val = r.split(' ')
            rooms.append(Room(r_num, r_act, int(r_val)))
            r_num += 1
        return cls(rooms)


class ControlClass:
    def __init__(self) -> None:
        self.data: Base = Base.FromInput()
        self.player: Player = Player()
        if DEBUG: print(self.data)

    def run(self) -> None:
        for r in self.data.rooms:
            self.player.loc = r.num
            if r.act == 'potion':
                self.player.heal(r.val)
            elif r.act == 'chest':
                self.player.loot(r.val)
            else:
                if not self.player.fight(r.act, r.val): break

        if self.player.isalive():
            print("You've made it!")
            print(f"Bitcoins: {self.player.bitcoins}")
            print(f"Health: {self.player.hp}")
        else:
            print(f'Best room: {self.player.loc}')



def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        if DEBUG: print(test_run)
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
