import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Join WebStars now for free, at www.web-stars.com',
        'You can also support our partners:',
        'Internet - www.internet.com',
        'WebSpiders - www.webspiders101.com',
        'Sentinel - www.sentinel.-ko',
    ),
    (
        'Need information about cheap hotels in London?',
        'You can check us at www.london-hotels.co.uk !',
        'We provide the best services in London.',
        'Here are some reviews in some blogs:',
        'London Hotels are awesome! - www.indigo.bloggers.com',
        'I am very satisfied with their services - ww.ivan.bg',
        'Best Hotel Services! - www.rebel21.sedecrem.moc',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.re: str = r"(?P<generic>www.?[A-Za-z0-9]+([.-]?[A-Za-z0-9]+)+\.[a-z]+)"
        self.rg: str = 'generic'

    def run(self) -> None:
        rr: List[str] = list()
        while True:
            try:
                lin: str = input()
                if lin == '':
                    break
                for r in re.finditer(self.re, lin):
                    rr.append(r.group(self.rg))
            except (StopIteration, EOFError,) as _:
                break
        print('\n'.join(rr))


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
