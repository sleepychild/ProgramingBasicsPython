from typing import Dict


player: str = str()
goals: int = int()

in_str: str = str()
in_int: int = int()

while True:
    in_str = input()
    if in_str == 'END':
        break
    in_int = int(input())
    if in_int > goals:
        player = in_str
        goals = in_int
    if goals >= 10:
        break

print(f'{player} is the best player!')
print(f'He has scored {goals}', 'goals.' if goals < 3 else 'goals and made a hat-trick !!!')
