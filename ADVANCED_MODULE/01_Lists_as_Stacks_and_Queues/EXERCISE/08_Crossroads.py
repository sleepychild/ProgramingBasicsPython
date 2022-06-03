from collections import deque
from typing import Deque, Generator, Callable, Tuple


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "10",
        "5",
        "Mercedes",
        "green",
        "Mercedes",
        "BMW",
        "Skoda",
        "green",
        "END",
    ),
    (
        "9",
        "3",
        "Mercedes",
        "Hummer",
        "green",
        "Hummer",
        "Mercedes",
        "green",
        "END",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    green_light_interval: int = int(input())
    free_window_interval: int = int(input())

    total_cars_passed: int = int()

    cars: Deque[str] = deque()

    crash: bool = bool()

    while True:
        line_in: str = input()
        if line_in == "END":
            break
        elif line_in == "green":
            g: int = green_light_interval
            while g > 0 and cars:
                car: str = cars.pop()
                total_cars_passed += 1
                g -= len(car)
            if g < 0 and free_window_interval < len(car[g:]):
                print("A crash happened!")
                print(f"{car} was hit at {car[g+free_window_interval]}.")
                crash = True
                break
        else:
            cars.appendleft(line_in)

    if not crash:
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
