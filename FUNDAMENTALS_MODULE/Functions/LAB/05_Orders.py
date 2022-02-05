from typing import Tuple

price_list_items: Tuple[str] = ('coffee', 'coke', 'water', 'snacks')
price_list_values: Tuple[str] = (1.5, 1.4, 1.0, 2.0)

print(f'{price_list_values[price_list_items.index(input())]*int(input()):.2f}')
