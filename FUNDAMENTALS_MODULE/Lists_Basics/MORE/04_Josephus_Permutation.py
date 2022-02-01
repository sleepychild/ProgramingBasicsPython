from typing import List

# people_list_in: List[str] = '1 2 3 4 5 6 7'.split(' ')
# people_step: int = int('3') -1

# people_list_in: List[str] = '10 5 65 104 1 0 2'.split(' ')
# people_step: int = int('8') -1

people_list_in: List[str] = input().split(' ')
people_step: int = int(input()) -1

people_list_out: List[str] = list()
people_list_len: int = len(people_list_in)
people_pos: int = int()

while people_list_len > 0:
    people_pos += people_step
    try:
        people_list_out.append(people_list_in.pop(people_pos))
    except IndexError as _:
        people_pos %= people_list_len
        people_list_out.append(people_list_in.pop(people_pos))
    people_list_len = len(people_list_in)

print(f'[{",".join(people_list_out)}]')
