from typing import List

l: List[str] = list(input())

# l: List[str] = list('a3')
# l: List[str] = list('aSd2&5s@1')
# l: List[str] = list('a10b10')

p: int = int()
r: str = str()
t: str = str()
d: str = str()

while True:
    try:
        if l[p].isdigit():
            d: str = str()
            while l[p].isdigit():
                d += l[p]
                p += 1
            r += t*int(d)
            t: str = str()
        else:
            t += l[p].upper()
            p += 1
    except IndexError as _:
        r += t*int(d)
        break

print(f'Unique symbols used: {len(set([c.upper() for c in l if not c.isdigit()]))}')
print(r)
