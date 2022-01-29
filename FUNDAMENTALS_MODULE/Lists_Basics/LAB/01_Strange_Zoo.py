from typing import List, Tuple

def hbt_sorter(e: str) -> int:
    parts: Tuple[str] = ('head', 'body', 'tail',)
    e_lower: str = e.lower()
    for part in parts:
        if e_lower.find(part) != -1:
            return parts.index(part)

str_list: List[str] = [input(),input(),input(),]
str_list.sort(key=hbt_sorter)

print(str_list)
