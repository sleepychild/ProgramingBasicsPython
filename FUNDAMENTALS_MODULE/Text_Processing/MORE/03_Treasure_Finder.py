from typing import List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "1 2 1 3",
        "ikegfp'jpne)bv=41P83X@",
        "ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA",
        "find",
    ),
    (
        "0",
        "&junk&  <nowhere>"
        "find",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    key: List[int] = [int(k) for k in input().split()]
    while True:
        lin: str = input()
        if lin == 'find':
            break
        data_in: List[str] = list(lin)
        data_out: List[str] = list()
        for di, dd in enumerate(data_in):
            data_out.append(chr(ord(dd) - key[di % len(key)]))
        data_out_str: str = ''.join(data_out)
        try:
            treasure: str = data_out_str.split('&')[1]
            location: str = data_out_str.split('<')[1].split('>')[0]
        except Exception as e:
            if DEBUG:
                print(e)
        else:
            print(f"Found {treasure} at {location}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
