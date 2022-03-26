from typing import List


lin: str = input()

ops: List[str] = lin.split()
ops_res: List[float] = list()


def c_in_al(c: str) -> int:
    return ord(c.lower()) - 96


for o in ops:
    r: float = float()
    f: str = o[0]
    l: str = o[-1]
    n: int = int(o[1:-1])

    if f.isupper():
        r = n / c_in_al(f)
    else:
        r = n * c_in_al(f)

    if l.isupper():
        r -= c_in_al(l)
    else:
        r += c_in_al(l)

    ops_res.append(r)

print(f"{sum(ops_res):.2f}")
