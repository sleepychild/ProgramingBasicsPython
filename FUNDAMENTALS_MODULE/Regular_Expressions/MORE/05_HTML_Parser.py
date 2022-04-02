import re
from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '<html>\n<head><title>Some title</title></head>\n<body>Here<p> is some </p>content <a href="www.somesite.com">\nclick</body>\n</html>',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    html_str: str = input()
    if DEBUG:
        print(html_str)

    html_str: str = html_str.replace('\n', '')
    if DEBUG:
        print(html_str)

    print(f"Title: {re.search(r'<title>(?P<title>.*)</title>', html_str).group('title')}")

    html_str: str = re.search(
        r'<body>(?P<body>.*)<\/body>', html_str
    ).group('body')
    if DEBUG:
        print(html_str)

    print(f"Content: {re.sub(r'<.*?>', '', html_str)}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
