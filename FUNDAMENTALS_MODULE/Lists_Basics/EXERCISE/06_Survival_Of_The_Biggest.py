from typing import List

def list_int_str(list_in: List[int]) -> List[str]:
    return [str(el) for el in list_in]

def list_str_int(list_in: List[str]) -> List[int]:
    return [int(el) for el in list_in]

numbers: List[int] = list_str_int(input().split(' '))
numbers_out: List[int] = numbers.copy()
numbers_out.sort()
numbers_out = numbers_out[int(input()):]

print(', '.join(list_int_str(list(filter(lambda n: n in numbers_out, numbers)))))
