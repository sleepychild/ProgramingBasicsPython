from typing import List

numbers_in: List[int] = [ int(i) for i in input().split(' ') ]
avg = sum(numbers_in) / len(numbers_in)
numbers_out: List[int] = sorted(list(filter(lambda e: e > avg, numbers_in)), reverse=True)[:5]
print('No' if len(numbers_out) == 0 else ' '.join([ str(i) for i in numbers_out ]))
