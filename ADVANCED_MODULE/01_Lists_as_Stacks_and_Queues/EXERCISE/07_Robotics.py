from typing import Generator, Callable, Tuple, List, Deque
from collections import deque

from datetime import datetime, timedelta

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "ROB-15;SS2-10;NX8000-3",
        "8:00:00",
        "detail",
        "glass",
        "wood",
        "apple",
        "End",
    ),
    (
        "ROB-8",
        "7:59:59",
        "detail",
        "glass",
        "wood",
        "sock",
        "End",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


STRP: str = "%H:%M:%S"
STRF: str = "[%H:%M:%S]"


class Robot:
    def __init__(self, name: str, process_time: int) -> None:
        self.name: str = name
        self.process_time: int = process_time
        self.available_time: datetime = datetime.strptime("00:00:00", STRP)

    def available(self, current_time: datetime) -> bool:
        return self.available_time <= current_time

    def process(self, product: str, current_time: datetime) -> str:
        self.available_time: datetime = current_time + timedelta(
            seconds=self.process_time
        )
        return f"{self.name} - {product} {current_time.strftime(STRF)}"

    def __str__(self) -> str:
        return (
            f"{self.name} | {self.process_time} | {self.available_time.strftime(STRF)}"
        )

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def from_string(cls, string_in: str) -> "Robot":
        name, ptime = string_in.split("-")
        return cls(name, int(ptime))


def solution():
    robots: List[Robot] = list()
    products: Deque[str] = deque()

    for r in input().split(";"):
        robots.append(Robot.from_string(r))

    line_active: bool = True
    ticks: int = int()
    start_time: datetime = datetime.strptime(input(), STRP)

    if DEBUG:
        print(robots)
        print(start_time.strftime(STRF))

    while True:
        ticks += 1
        current_time: datetime = start_time + timedelta(seconds=ticks)

        if line_active:
            line_in: str = input()
            if line_in == "End":
                line_active = False
            else:
                products.append(line_in)

        if not products:
            break

        product_assigned: bool = False
        for robot in robots:
            if robot.available(current_time):
                print(robot.process(products.pop(), current_time))
                product_assigned = True
                break

        if not product_assigned:
            products.rotate()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
