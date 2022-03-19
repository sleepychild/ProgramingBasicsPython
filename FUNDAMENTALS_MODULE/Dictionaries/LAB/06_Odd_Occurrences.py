from typing import List


lin: List[str] = input().lower().split()
lout: List[str] = list()

while len(lin) > 0:
    el: str = lin[0]
    if (lin.count(el) % 2) != 0:
        lout.append(el)
    while el in lin:
        lin.remove(el)

print(' '.join(lout))
