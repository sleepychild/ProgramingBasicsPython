from typing import List

num_list: List[int] = [ int(x) for x in input().split(' ') ]

print(f'The minimum number is {min(num_list)}')
print(f'The maximum number is {max(num_list)}')
print(f'The sum number is: {sum(num_list)}')
