from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Light | Peter',
        'Dark | Kim',
        'Light | Kim',
        'Lumpawaroo',
    ),
    (
        'Lighter | Royal',
        'Darker | DCay',
        'Ivan Ivanov -> Lighter',
        'DCay -> Lighter',
        'Lumpawaroo',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.force_sides: List[str] = list()
        self.force_users: Dict[str, int] = dict()

    def or_func(self, fs: str, fu: str) -> None:
        if fu in self.force_users:
            return

        if fs not in self.force_sides:
            self.force_sides.append(fs)

        self.force_users[fu] = self.force_sides.index(fs)

    def to_func(self, fu: str, fs: str) -> None:
        if fs not in self.force_sides:
            self.force_sides.append(fs)

        if fu in self.force_users:
            del self.force_users[fu]

        self.force_users[fu] = self.force_sides.index(fs)
        print(f'{fu} joins the {fs} side!')

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'Lumpawaroo':
                break
            elif lin.find(' | ') != -1:
                self.or_func(*lin.split(' | '))
            elif lin.find(' -> ') != -1:
                self.to_func(*lin.split(' -> '))

        if DEBUG:
            print(self.force_sides)
            print(self.force_users)

        for fs_i, fs_n in enumerate(self.force_sides):
            fs_m: List[str] = [
                k for (k, v) in self.force_users.items() if v == fs_i]
            if fs_m:
                print(f"Side: {fs_n}, Members: {len(fs_m)}")
                for m in fs_m:
                    print(f'! {m}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
