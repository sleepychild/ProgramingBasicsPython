from typing import List

num_strings: int = int(input())
search_substring: str = input()
strings_list: List[str] = list()

for _ in range(num_strings):
    strings_list.append(input())

print(strings_list)
print(list(filter(lambda e: e.find(search_substring) != -1, strings_list)))
