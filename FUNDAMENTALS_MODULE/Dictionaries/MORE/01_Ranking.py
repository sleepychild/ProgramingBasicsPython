from typing import Dict, List, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Part One Interview:success',
        'JS Fundamentals:fundExam',
        'C# Fundamentals:fundPass',
        'Algorithms:fun',
        'end of contests',
        'C# Fundamentals=>fundPass=>Tanya=>350',
        'Algorithms=>fun=>Tanya=>380',
        'Part One Interview=>success=>Nikola=>120',
        'Java Basics Exam=>wrong_pass=>Teo=>400',
        'Part One Interview=>success=>Tanya=>220',
        'OOP Advanced=>password123=>Kay=>231',
        'C# Fundamentals=>fundPass=>Tanya=>250',
        'C# Fundamentals=>fundPass=>Nikola=>200',
        'JS Fundamentals=>fundExam=>Tanya=>400',
        'end of submissions',
    ),
    (
        'Java Advanced:funpass',
        'Part Two Interview:success',
        'Math Concept:asdasd',
        'Java Web Basics:forrF',
        'end of contests',
        'Math Concept=>ispass=>Monika=>290',
        'Java Advanced=>funpass=>Simona=>400',
        'Part Two Interview=>success=>Drago=>120',
        'Java Advanced=>funpass=>Petyr=>90',
        'Java Web Basics=>forrF=>Simona=>280',
        'Part Two Interview=>success=>Petyr=>0',
        'Math Concept=>asdasd=>Drago=>250',
        'Part Two Interview=>success=>Simona=>200',
        'end of submissions',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.contests: Dict = dict()
        self.users: Dict = dict()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'end of contests':
                break
            contest, password = lin.split(':')
            self.contests.update({contest: password})

        while True:
            lin: str = input()
            if lin == 'end of submissions':
                break
            contest, password, user, points = lin.split("=>")
            if contest in self.contests and password == self.contests[contest]:
                if user not in self.users:
                    self.users[user] = {'contests': dict(), 'tottal_points': int()}
                if contest not in self.users[user]['contests']:
                    self.users[user]['contests'][contest] = int(points)
                else:
                    self.users[user]['contests'][contest] = max(int(points), self.users[user]['contests'][contest])

        best_user: Dict = {
            'name': str(),
            'pts': int()
        }

        for user_k, user_v in self.users.items():
            user_v['tottal_points'] = sum(user_v['contests'].values())
            if best_user['pts'] < user_v['tottal_points']:
                best_user['name'] = user_k
                best_user['pts'] = user_v['tottal_points']

        print(f"Best candidate is {best_user['name']} with total {best_user['pts']} points.")
        print('Ranking:')
        for user_k, user_v in sorted(self.users.items()):
            print(user_k)
            for contest_name, contest_pts in sorted(user_v['contests'].items(), key=lambda item: item[1], reverse=True):
                print(f'#  {contest_name} -> {contest_pts}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
