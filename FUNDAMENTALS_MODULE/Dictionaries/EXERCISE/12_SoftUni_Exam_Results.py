from audioop import reverse
from typing import List, Dict, Tuple, Generator, Callable, Union, Any
from enum import Enum

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Peter-Java-84',
        'George-C#-84',
        'George-C#-70',
        'Katy-C#-94',
        'exam finished',
    ),
    (
        'Peter-Java-91',
        'George-C#-84',
        'Katy-Java-90',
        'Katy-C#-50',
        'Katy-banned',
        'exam finished',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class Base:

    @classmethod
    def FromInput(cls) -> 'Base':
        print(input())
        return cls()


class ControlClass:

    def __init__(self) -> None:
        self.users: Dict[str, Any] = dict()
        self.langs: List[str] = list()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'exam finished':
                break
            elif lin.endswith('-banned'):
                u: str = lin.split('-')[0]
                if u not in self.users:
                    self.users[u] = dict()
                self.users[u]['banned'] = True
            else:
                u, l, p = lin.split('-')
                if l not in self.langs:
                    self.langs.append(l)
                if u not in self.users:
                    self.users[u] = {
                        "banned": False,
                        "res": list()
                    }
                self.users[u]["res"].append({
                    "lng": self.langs.index(l),
                    "pts": int(p)
                })
                self.users[u]["res"].sort(key=lambda e: e["pts"], reverse=True)

        if DEBUG:
            print(self.users)
            print(self.langs)

        print('Results:')
        for k, v in self.users.items():
            if not v['banned']:
                print(f"{k} | {v['res'][0]['pts']}")
        print('Submissions:')
        res: List[int] = list()
        for l in self.users.values():
            for ll in l['res']:
                res.append(ll['lng'])
        for l_i, l_n in enumerate(self.langs):
            print(f'{l_n} - {res.count(l_i)}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
