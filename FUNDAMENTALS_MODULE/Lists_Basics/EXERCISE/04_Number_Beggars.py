from typing import List

ammounts: List[int] = list()

for a in input().split(', '):
    ammounts.append(int(a))

beggars_count: int = int(input())

ammounts_count: int = len(ammounts)
beggars: List[int] = [0] * beggars_count

for beggar_i in range(len(beggars)):
    for ammount_i in range(beggar_i,ammounts_count, beggars_count):
        beggars[beggar_i] += ammounts[ammount_i]

print(beggars)
