from typing import List

str_list: List[str] = [input(),input(),input(),]
str_list[0], str_list[2] = str_list[2], str_list[0]

print(str_list)
