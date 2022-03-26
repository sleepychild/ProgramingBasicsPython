from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Peter -> Algo -> 400',
        'George -> Algo -> 300',
        'Simo -> Algo -> 200',
        'Peter -> DS -> 150',
        'Mariya -> DS -> 600',
        'no more time',
    ),
    (
        'Peter -> OOP -> 350',
        'George -> OOP -> 250',
        'Simo -> Advanced -> 600',
        'George -> OOP -> 300',
        'Prakash -> OOP -> 300',
        'Prakash -> Advanced -> 250',
        'Ani -> JSCore -> 400',
        'no more time',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.contests: List = list()
        self.users: Dict = dict()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'no more time':
                break

            user, contest, points = lin.split(' -> ')

            if contest not in self.contests:
                self.contests.append(contest)

            if user not in self.users:
                self.users[user] = dict()
                self.users = dict(sorted(self.users.items()))

            if contest in self.users[user]:
                self.users[user][contest] = max(
                    int(points), self.users[user][contest])
            else:
                self.users[user][contest] = int(points)

        for contest in self.contests:
            contest_users: Dict = dict(sorted(
                {k: v[contest] for k, v in self.users.items() if contest in v}.items(), key=lambda i: i[1], reverse=True
            ))
            print(f"{contest}: {len(contest_users)} participants")
            for ki, kv in enumerate(contest_users.keys(), 1):
                print(f"{ki}. {kv} <::> {contest_users[kv]}")

        user_standings: Dict = dict(sorted(
            {k: sum(v.values()) for k, v in self.users.items()}.items(), key=lambda i: i[1], reverse=True
        ))

        print("Individual standings:")
        for ui, uk in enumerate(user_standings.items(), 1):
            print(f"{ui}. {uk[0]} -> {uk[1]}")

def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
