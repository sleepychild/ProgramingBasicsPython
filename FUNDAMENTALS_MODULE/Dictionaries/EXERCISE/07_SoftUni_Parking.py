from typing import Dict, List, Tuple, Generator, Callable, Union
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        'register John CS1234JS',
        'register George JAVA123S',
        'register Andy AB4142CD',
        'register Jesica VR1223EE',
        'unregister Andy',
    ),
    (
        '4',
        'register Jony AA4132BB',
        'register Jony AA4132BB',
        'register Linda AA9999BB',
        'unregister Jony',
    ),
    (
        '6',
        'register Jacob MM1111XX',
        'register Anthony AB1111XX',
        'unregister Jacob',
        'register Joshua DD1111XX',
        'unregister Lily',
        'register Samantha AA9999BB',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.parking: Dict[str, str] = dict()

    def run(self) -> None:
        for _ in range(int(input())):
            line_in: str = input()
            if line_in.startswith('register'):
                _c, u, l = line_in.split()
                if u in self.parking:
                    print(
                        f"ERROR: already registered with plate number {self.parking[u]}")
                else:
                    self.parking[u] = l
                    print(f"{u} registered {l} successfully")
            elif line_in.startswith('unregister'):
                _c, u = line_in.split()
                if u in self.parking:
                    del self.parking[u]
                    print(f"{u} unregistered successfully")
                else:
                    print(f"ERROR: user {u} not found")
        for k, v in self.parking.items():
            print(f'{k} => {v}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
