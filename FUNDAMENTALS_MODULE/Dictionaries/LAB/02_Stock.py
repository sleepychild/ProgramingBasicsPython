from typing import List, Dict

list_stocks: List[str] = input().split()
list_search: List[str] = input().split()

dict_stocks: Dict = dict(zip(list_stocks[0::2], [int(i) for i in list_stocks[1::2]]))

for search in list_search:
    try:
        item_val: int = dict_stocks[search]
        print(f"We have {item_val} of {search} left")
    except KeyError as e:
        print(f"Sorry, we don't have {e.args[0]}")
