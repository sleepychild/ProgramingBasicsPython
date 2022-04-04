import re
from typing import Dict, Tuple, Generator, Callable


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '@@@@green@*/10/@yel0w@*26*#red#####//8//@limon*@*23*@@@red#*/%^&/6/@gree_een@/notnumber/###purple@@@@@*$%^&*/5/',
    ),
    (
        '#@##@red@#/8/@rEd@/2/#@purple@////10/',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

egg_hunt = re.compile(r'[@|#]+(?P<color>[a-z]{3,})[@|#]+[^A-Za-z0-9]*\/+(?P<count>\d+)\/*')

def solution():
    for egg_match in egg_hunt.finditer(input()):
        egg: Dict[str, str] = egg_match.groupdict()
        print(f"You found {egg['count']} {egg['color']} eggs!")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
