from typing import List

data_in: List[int] = [ int(x) for x in input().split(', ') ]
evens: List[int] = list()
for i in range(len(data_in)):
    if (data_in[i] % 2) == 0:
        evens.append(i)
print(evens)
