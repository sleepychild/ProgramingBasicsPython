from typing import Deque, Tuple, Generator, Callable
from collections import deque

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "3",
        "1 5",
        "10 3",
        "3 4",
    ),
    (
        "5",
        "22 5",
        "14 10",
        "52 7",
        "21 12",
        "36 9",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


class Pump:
    def __init__(self, gas: int, kil: int) -> None:
        self.gas: int = gas
        self.kil: int = kil

    def __str__(self) -> str:
        return f"gas: {self.gas} kil: {self.kil}"

    def __repr__(self) -> str:
        return self.__str__()


class Truck:
    def __init__(self) -> None:
        self.gas: int = int()

    def travel(self, circle: Deque) -> bool:
        for pump in circle:
            self.gas += pump.gas
            self.gas -= pump.kil
            if self.gas < 0:
                return False
        return True


def solution():
    pumps: Deque = deque()
    for _ in range(int(input())):
        pumps.append(Pump(*[int(v) for v in input().split()]))

    if DEBUG:
        print(pumps)

    distance: int = sum([p.kil for p in pumps])
    gas_total: int = sum([p.gas for p in pumps])

    if DEBUG:
        print(f"dist: {distance} gas ttl: {gas_total}")

    for i in range(len(pumps)):
        truck: Truck = Truck()
        tmp_pumps: Deque = pumps.copy()
        tmp_pumps.rotate(-i)
        if truck.travel(tmp_pumps):
            print(i)
            break


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
