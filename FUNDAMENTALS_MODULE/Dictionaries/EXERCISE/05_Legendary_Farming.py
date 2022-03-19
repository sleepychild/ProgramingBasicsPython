from typing import ClassVar, Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '3 Motes 5 stones 5 Shards',
        '6 leathers 255 fragments 7 Shards',
    ),
    (
        '123 silver 6 shards 8 shards 5 motes',
        '9 fangs 75 motes 103 MOTES 8 Shards',
        '86 Motes 7 stones 19 silver',
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
    __LEGENDARY_ITEMS: ClassVar[Dict[str, Dict[str, Union[str, int]]]] = {
        "Shadowmourne": {
            "cost": 250,
            "currency": "shards"
        },
        "Valanyr": {
            "cost": 250,
            "currency": "fragments"
        },
        "Dragonwrath": {
            "cost": 250,
            "currency": "motes"
        }
    }

    def __init__(self) -> None:
        self.inventory: Dict[str, int] = {
            "shards": 0,
            "fragments": 0,
            "motes": 0
        }

    def run(self) -> None:

        while True:
            try:
                collected: List = [
                    int(i) if i.isnumeric() else i.lower() for i in input().split()
                ]
                if DEBUG:
                    print(collected)
            except StopIteration:
                if DEBUG:
                    print('StopIteration')
                return
            else:
                for c_k, c_v in zip(collected[1::2], collected[0::2]):
                    if DEBUG:
                        print(f"clct: {c_k} {c_v}")
                    if c_k in self.inventory:
                        self.inventory[c_k] += c_v
                    else:
                        self.inventory[c_k] = c_v

                    for LI_K, LI_V in self.__LEGENDARY_ITEMS.items():
                        if (LI_V["currency"] in self.inventory) and (self.inventory[LI_V["currency"]] >= LI_V["cost"]):
                            print(f"{LI_K} obtained!")
                            self.inventory[LI_V["currency"]] -= LI_V["cost"]
                            return

    def __str__(self) -> str:
        rtrn_str: str = str()
        for k, v in self.inventory.items():
            rtrn_str += f"{k}: {v}\n"
        return rtrn_str


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()
    print(str(ctrl))


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
