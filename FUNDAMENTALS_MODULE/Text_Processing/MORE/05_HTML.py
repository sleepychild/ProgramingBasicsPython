from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'SoftUni Article',
        'Some content of the SoftUni article',
        'some comment',
        'more comment',
        'last comment',
        'end of comments',
    ),
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    print(f"""<h1>
    {input()}
</h1>
<article>
    {input()}
</article>""")
    while True:
        lin: str = input()
        if lin == 'end of comments':
            break
        print(f"""<div>
    {lin}
</div>""")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
