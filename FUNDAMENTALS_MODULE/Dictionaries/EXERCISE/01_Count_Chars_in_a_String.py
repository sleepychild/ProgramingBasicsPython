from typing import List


c_l: List[str] = list(input())

while len(c_l) > 0:
    c: str = c_l[0]
    if not c.isspace():
        print(f"{c} -> {c_l.count(c)}")
    while c in c_l:
        c_l.remove(c)
