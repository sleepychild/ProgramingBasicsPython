import re
from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '>>Sofa<<312.23!3',
        '>>TV<<300!5',
        '>Invalid<<!5',
        'Purchase',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.re: str = r"(^|\b)(?P<generic>(Purchase|[>]{2}(?P<item>\w+)[<]{2}(?P<price>(?P<sign>[+-]?)(?P<whole>[0]|[1-9]\d*)(?P<decimal>\.\d+)?)!(?P<qty>\d+)))($|\b])"
        self.rg: str = 'generic'

    def run(self) -> None:
        match_list: List[Dict[str, str]] = list()
        while True:
            try:
                r = re.search(self.re, input())
                if r:
                    td: Dict[str, str] = r.groupdict()
                    if td['generic'] == 'Purchase':
                        break
                    else:
                        match_list.append(td)
            except StopIteration as _:
                break
        if DEBUG:
            for m in match_list:
                print(m)
        cost: float = float()
        print('Bought furniture:')
        for m in match_list:
            print(m['item'])
            cost += int(m['qty']) * float(m['price'])
        print(f"Total money spend: {cost:.2f}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
