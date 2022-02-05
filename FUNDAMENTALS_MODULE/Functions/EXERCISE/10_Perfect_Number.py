from typing import List

number: int = int(input())
prop_pos_divs: List[int] = list()

for d in range(1, number//2+1):
    if number % d == 0:
        prop_pos_divs.append(d)

print('We have a perfect number!' if number == sum(prop_pos_divs) else "It's not so perfect.")
