from typing import List

numbers: List[int] = [ int(x) for x in input().split(', ') ]

for g in range(10, max(numbers)+10, 10):
    print(f"Group of {g}'s: {list(filter(lambda x: g >= x > g-10, numbers))}")
