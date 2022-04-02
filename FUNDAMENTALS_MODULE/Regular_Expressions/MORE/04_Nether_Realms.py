import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'M3ph-0.5s-0.5t0.0**',
    ),
    (
        'M3ph1st0**, Azazel',
    ),
    (
        'Gos/ho',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class Daemon:
    health_ptrn = re.compile(
        r'[^0-9+\-*\/.]'
    )
    base_dmg_ptrn = re.compile(
        r'(?P<number>(?P<sign>[-|+]?)(?P<whole>[0]|[1-9]\d*)(?P<decimal>\.\d+)?)'
    )
    alter_dmg_ptrn = re.compile(
        r'(\*|\/)'
    )

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = int()
        self.damage: float = float()

        self._calc_health()
        self._cals_damage()

    def _calc_health(self) -> None:
        self.health = sum(
            [ord(m)for m in self.health_ptrn.findall(self.name)]
        )

    def _cals_damage(self) -> None:
        self.damage: float = sum(
            [float(m[0]) for m in self.base_dmg_ptrn.findall(self.name)]
        )
        for a in self.alter_dmg_ptrn.findall(self.name):
            self.damage = self.damage * 2 if a == '*' else self.damage / 2

    def __str__(self) -> str:
        return f"{self.name} - {self.health} health, {self.damage:.2f} damage"
    
    def __repr__(self) -> str:
        return str(self)

def solution():
    lin: str = input()
    demons: List[Daemon] = sorted([Daemon(d.strip()) for d in lin.split(',')], key=lambda d: d.name)
    for d in demons:
        print(d)


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
