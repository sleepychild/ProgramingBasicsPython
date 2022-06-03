from collections import deque
from typing import Deque, Generator, Callable, List, Tuple


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "50",
        "2",
        "11 10 5 11 10 20",
        "15 13 16",
        "1500",
    ),
    (
        "20",
        "6",
        "14 13 12 11 10 5",
        "13 3 11 10",
        "800",
    ),
    (
        "33",
        "1",
        "12 11 10",
        "10 20 30",
        "100",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution():
    bullet_cost: int = int(input())
    gun_barrel_size: int = int(input())
    bullets: List[int] = [int(b) for b in input().split()]
    locks: List[int] = [int(l) for l in input().split()]
    prize: int = int(input())

    ammo: int = gun_barrel_size
    bullet_expence: int = int()

    while bullets and locks:

        if bullets.pop() <= locks[0]:
            print("Bang!")
            locks.pop(0)
        else:
            print("Ping!")

        bullet_expence += bullet_cost
        ammo -= 1

        if ammo == 0 and bullets:
            ammo += gun_barrel_size
            print("Reloading!")

    if locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        print(f"{len(bullets)} bullets left. Earned ${prize-bullet_expence}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
