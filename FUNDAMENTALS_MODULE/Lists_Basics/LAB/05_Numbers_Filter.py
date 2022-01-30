from operator import truediv
from typing import List

def even(n: int) -> bool:
    return (n % 2) == 0

def odd(n: int) -> bool:
    return (n % 2) != 0

def negative(n: int) -> bool:
    return n < 0

def positive(n: int) -> bool:
    return n >= 0

numbers_list: List[int] = list()

for _ in range(int(input())):
    numbers_list.append(int(input()))

print(list(filter(locals()[input()], numbers_list)))
