from typing import List

numbers_list: List[int] = [ int(x) for x in input() ]

print(f'Odd sum = {sum(filter(lambda n: (n % 2) != 0, numbers_list))}, Even sum = {sum(filter(lambda n: (n % 2) == 0, numbers_list))}')
