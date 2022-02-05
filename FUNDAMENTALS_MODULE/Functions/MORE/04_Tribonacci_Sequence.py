from typing import List

num: List[int] = [1]

def tribonacci(num: List[int]) -> None:    
    num.append(sum(num[-3:]))

for _ in range(int(input())-1):
    tribonacci(num)

print(' '.join([str(x) for x in num]))
