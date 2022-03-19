from typing import List
list_stocks: List[str] = input().split()
print(dict(zip(list_stocks[0::2], [int(i) for i in list_stocks[1::2]])))
