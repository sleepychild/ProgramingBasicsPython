from typing import List

empl_hpy: List[int] = [int(x) for x in input().split(' ')]
hpy_indx: int = int(input())

empl_hpy = [ x * hpy_indx for x in empl_hpy ]

hpy_avg: float = sum(empl_hpy) / len(empl_hpy)

happy_count: int = len(list(filter(lambda x: x >= hpy_avg, empl_hpy)))
total_count: int = len(empl_hpy)

msg: str = 'Employees are happy!' if happy_count >= (total_count//2) else 'Employees are not happy!'

print(f'Score: {happy_count}/{total_count}. {msg}')
