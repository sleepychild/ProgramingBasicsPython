from typing import List

nums: List[int] = [int(input()), int(input()), int(input())]

if 0 in nums:
    print('zero')
elif (len(list(filter(lambda x: x < 0, nums))) % 2) == 0:
    print('positive')
else:
    print('negative')
