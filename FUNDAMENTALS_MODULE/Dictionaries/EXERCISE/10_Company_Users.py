from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'SoftUni -> AA12345',
        'SoftUni -> BB12345',
        'Microsoft -> CC12345',
        'HP -> BB12345',
        'End',
    ),
    (
        'SoftUni -> AA12345',
        'SoftUni -> CC12344',
        'Lenovo -> XX23456',
        'SoftUni -> AA12345',
        'Movement -> DD11111',
        'End',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.cmpny: Dict[str, List[str]] = dict()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'End':
                break

            c, e = lin.split(' -> ')

            if c not in self.cmpny:
                self.cmpny[c] = list()

            if e not in self.cmpny[c]:
                self.cmpny[c].append(e)

        for k, v in self.cmpny.items():
            print(k)
            for e in v:
                print(f'-- {e}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
