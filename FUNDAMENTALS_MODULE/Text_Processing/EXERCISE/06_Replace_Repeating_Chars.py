from typing import List


lin: List[str] = list(input())
i: int = int()
while True:
    try:
        if lin[i] == lin[i+1]:
            lin.pop(i+1)
        else:
            i += 1
    except IndexError as e:
        break

print(''.join(lin))
