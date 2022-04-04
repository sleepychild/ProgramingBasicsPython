from typing import Dict, Tuple, Generator, Callable


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'New follower: George',
        'Like: George: 5',
        'New follower: George',
        'Log out',
    ),
    (
        'Like: Katy: 3',
        'Comment: Katy',
        'New follower: Bob',
        'Blocked: Bob',
        'New follower: Amy',
        'Like: Amy: 4',
        'Log out',
    ),
    (
        'Blocked: Amy',
        'Comment: Amy',
        'New follower: Amy',
        'Like: Tom: 5',
        'Like: Ellie: 5',
        'Log out',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    followers: Dict[str, int] = dict()
    while True:
        lin: str = input()
        if lin == 'Log out':
            break
        if lin.startswith('New follower:'):
            flwr: str = lin.split(': ')[1]
            if flwr not in followers:
                followers[flwr] = {
                    'likes': 0,
                    'comments': 0,
                }
        elif lin.startswith('Like:'):
            flwr, likes = lin.split(': ')[1:]
            if flwr in followers:
                followers[flwr]['likes'] += int(likes)
            else:
                followers[flwr] = {
                    'likes': int(likes),
                    'comments': 0,
                }
        elif lin.startswith('Comment:'):
            flwr: str = lin.split(': ')[1]
            if flwr in followers:
                followers[flwr]['comments'] += 1
            else:
                followers[flwr] = {
                    'likes': 0,
                    'comments': 1,
                }
        elif lin.startswith('Blocked:'):
            flwr: str = lin.split(': ')[1]
            if flwr in followers:
                del followers[flwr]
            else:
                print(f"{flwr} doesn't exist.")
    print(f'{len(followers)} followers')
    for flwr_name, flwr_data in followers.items():
        print(f"{flwr_name}: {flwr_data['likes']+flwr_data['comments']}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
