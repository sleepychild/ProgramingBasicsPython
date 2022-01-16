from math import floor

group_size: int = int(input())
days: int = int(input()) + 1

coins: int = int()

for day in range(1, days):
    coins += 50

    if day % 10 == 0:
        group_size -= 2
    
    if day % 15 == 0:
        group_size += 5
        coins -= group_size * 2

    coins -= group_size * 2

    if day % 3 == 0:
        coins -= group_size * 3
    
    if day % 5 == 0:
        coins += group_size * 20

print(f'{group_size} companions received {floor(coins/group_size)} coins each.')
