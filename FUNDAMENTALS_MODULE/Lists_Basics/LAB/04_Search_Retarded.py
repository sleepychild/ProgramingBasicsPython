from typing import List

num_strings: int = int(input())
search_substring: str = input()
strings_list: List[str] = list()
filtered_strings_list: List[str] = list()

for _ in range(num_strings):
    strings_list.append(input())

print(strings_list)

for string in strings_list:
    if string.find(search_substring) != -1:
        filtered_strings_list.append(string)

print(filtered_strings_list)
