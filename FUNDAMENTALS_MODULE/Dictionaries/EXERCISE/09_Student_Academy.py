from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '5',
        'John',
        '5.5',
        'John',
        '4.5',
        'Alice',
        '6',
        'Alice',
        '3',
        'George',
        '5',
    ),
    (
        '5',
        'Amanda',
        '3.5',
        'Amanda',
        '4',
        'Rob',
        '5.5',
        'Christian',
        '5',
        'Robert',
        '6',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.students: Dict[str, List[float]] = dict()

    def run(self) -> None:
        for _ in range(int(input())):
            sn: str = input()
            sg: float = float(input())

            if sn not in self.students:
                self.students[sn] = list()

            self.students[sn].append(sg)

        for k, v in self.students.items():
            sa: float = sum(v) / len(v)
            if sa >= 4.50:
                print(f"{k} -> {sa:.2f}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
