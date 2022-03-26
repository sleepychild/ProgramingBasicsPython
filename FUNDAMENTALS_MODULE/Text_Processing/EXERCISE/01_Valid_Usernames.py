from typing import List

names: List[str] = input().split(', ')


def name_filter(name) -> bool:
    if not (16 >= len(name) >= 3):
        return False
    for c in name:
        if not c.isalnum() and c not in ('-', '_'):
            return False
    return True


for name in filter(name_filter, names):
    print(name)
