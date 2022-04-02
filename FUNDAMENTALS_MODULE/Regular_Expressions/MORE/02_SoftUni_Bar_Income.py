import re
from typing import Dict, List, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        '%George%<Croissant>|2|10.3$',
        '%Peter%<Gum>|1|1.3$',
        '%Maria%<Cola>|1|2.4$',
        'end of shift',
    ),
    (
        '%InvalidName%<Croissant>|2|10.3$',
        '%Peter%<Gum>1.3$',
        '%Maria%<Cola>|1|2.4',
        '%Valid%<Valid>valid|10|valid20$',
        'end of shift',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


def solution():
    sales: List[Dict[str, Union[str, float, int]]] = list()
    total_income: float = float()
    while True:
        lin: str = input()
        if lin == 'end of shift':
            break
        sale: Dict[str, Union[str, float, int]] = dict()
        try:
            sale.update(re.search(r"%(?P<customer>[A-Z][a-z]+)%", lin).groupdict())
            sale.update(re.search(r"<(?P<product>\w+)>", lin).groupdict())
            sale.update(re.search(r"\|(?P<count>\d+)\|", lin).groupdict())
            sale.update(re.search(r"(?P<price>([0]|[1-9]\d*)(\.\d+)?)\$", lin).groupdict())
        except AttributeError as _:
            pass
        else:
            sale['count'] = int(sale['count'])
            sale['price'] = float(sale['price'])
            sale['total'] = sale['count'] * sale['price']
            if DEBUG:
                print(sale)
            print(f"{sale['customer']}: {sale['product']} - {sale['total']:.2f}")
            sales.append(sale)
            total_income += sale['total']
    if DEBUG:
        print(sales)
    print(f"Total income: {total_income:.2f}")


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
