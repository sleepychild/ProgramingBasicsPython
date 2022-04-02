import re
from typing import Dict, List, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '2',
        'STCDoghudd4=63333$D$0A53333',
        'EHfsytsnhf?8555&I&2C9555SR',
    ),
    (
        '3',
        'tt(''DGsvywgerx>6444444444%H%1B9444',
        'GQhrr|A977777(H(TTTT',
        'EHfsytsnhf?8555&I&2C9555SR',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


code_keys: List[str] = ['s', 't', 'a', 'r']


def start_enigma_decode(msg: str) -> str:
    msg_low: str = msg.lower()
    key: int = sum([msg_low.count(k) for k in code_keys])
    return ''.join([chr(ord(l)-key) for l in msg])


def solution():
    planets: List[Dict[str, Union[str, int]]] = list()
    for _ in range(int(input())):
        msg: str = start_enigma_decode(input())
        try:
            # planet: Dict[str, Union[str, int]] = re.search(r"(?P<name>(?<=@)[A-Za-z]+).*(?P<population>(?<=:)[1-9]\d+).*!(?P<atk_type>A|D)!.*(?P<soldier_count>(?<=->)[1-9]\d+)", msg).groupdict()
            planet: Dict[str, Union[str, int]] = re.search(r"@(?P<name>[A-Za-z]+)[^@\-!:>]*:(?P<population>[1-9]\d+)[^@\-!:>]*!(?P<atk_type>A|D)![^@\-!:>]*->(?P<soldier_count>[1-9]\d+)", msg).groupdict()
        except AttributeError as _:
            pass
        else:
            planets.append(planet)
    planets.sort(key=lambda i: i['name'])
    planets_attacked: List[Dict[str, Union[str, int]]] = list(filter(lambda i: i['atk_type'] == 'A', planets))
    planets_destroyed: List[Dict[str, Union[str, int]]] = list(filter(lambda i: i['atk_type'] == 'D', planets))
    print(f'Attacked planets: {len(planets_attacked)}')
    for plnt in planets_attacked:
        print(f"-> {plnt['name']}")
    print(f'Destroyed planets: {len(planets_destroyed)}')
    for plnt in planets_destroyed:
        print(f"-> {plnt['name']}")

if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
