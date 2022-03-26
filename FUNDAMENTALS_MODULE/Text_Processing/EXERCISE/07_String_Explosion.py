from typing import List


l: List[str] = list(input())

p: int = int()
c: int = int()

while True:
    try:
        if l[p] == '>':
            p += 1
            c += int(l[p])
        if c > 0:
            l.pop(p)
            c -= 1
        else:
            p += 1
    except IndexError as _:
        break

print(''.join(l))