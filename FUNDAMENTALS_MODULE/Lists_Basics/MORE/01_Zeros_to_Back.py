from typing import List
list_nums: List[int] = [int(x) for x in input().split(', ')]
zero_count: int = list_nums.count(0)
print(list(filter(lambda x: x != 0, list_nums))+[0]*zero_count)
