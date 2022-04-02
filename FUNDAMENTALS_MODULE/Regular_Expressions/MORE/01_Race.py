import re
from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'George, Peter, Bill, Tom',
        'G4e@55or%6g6!68e!!@',
        'R1@!3a$y4456@',
        'B5@i@#123ll',
        'G@e54o$r6ge#',
        '7P%et^#e5346r',
        'T$o553m&6',
        'end of race',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    racers: Dict[str, int] = {r: int() for r in input().split(', ')}
    while True:
        lin: str = input()
        if lin == 'end of race':
            break
        racer: str = ''.join(re.findall(r"[a-zA-Z]", lin))
        distance: int = sum([int(n) for n in re.findall(r"[0-9]", lin)])
        if DEBUG:
            print(racer, distance)
        if racer in racers:
            racers[racer] += distance
    racers_list: List[Dict[str, int]] = sorted(racers.items(), key=lambda i: i[1], reverse=True)
    try:
        print(f"1st place: {racers_list[0][0]}")
        print(f"2nd place: {racers_list[1][0]}")
        print(f"3rd place: {racers_list[2][0]}")
    except KeyError as _:
        pass


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
