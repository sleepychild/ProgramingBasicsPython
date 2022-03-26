from typing import List, Tuple

WINNING: Tuple[str] = ('@', '#', '$', '^',)

l: List[str] = [t.strip() for t in input().split(', ')]

for t in l:
    if len(t) != 20:
        print(f'invalid ticket')
        continue

    if (t[0] in WINNING) and (t == t[0] * 20):
        print(f'ticket "{t}" - 10{t[0]} Jackpot!')
        continue

    a, b = t[:10], t[10:]
    match: bool = False
    for i in range(9, 5, -1):
        if match:
            break
        for w in WINNING:
            if (w * i in a) and (w * i in b):
                print(f'ticket "{t}" - {i}{w}')
                match = True
                break
    if match:
        match = False
    else:
        print(f'ticket "{t}" - no match')
