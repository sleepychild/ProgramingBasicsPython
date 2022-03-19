from typing import Tuple, Generator, Callable, Dict, List
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Peter:123:programming basics',
        'John:5622:fundamentals',
        'Maya:89:fundamentals',
        'Lilly:633:fundamentals',
        'fundamentals',
    ),
    (
        'Alex:6:programming basics',
        'Maria:7:programming basics',
        'Kaloyan:9:advanced',
        'Todor:10:fundamentals',
        'programming_basics',
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
    params: List[str] = ['name', 'ID', 'course']

    def run(self) -> None:
        students: List[Dict] = list()
        while True:
            line_in: str = input()
            if line_in.count(':') == 2:
                students.append(dict(
                    zip(self.params, [int(e) if e.isnumeric() else e for e in line_in.split(':')])))
            else:
                break
        for student in list(filter(lambda s: s['course'] == line_in.replace('_', ' '), students)):
            print(f"{student['name']} - {student['ID']}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
