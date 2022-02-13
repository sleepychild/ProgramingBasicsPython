from typing import List

data_in: List[str] = list(input())

string_in: List[str] = list(filter(lambda l: not l.isnumeric() ,data_in))
numbers_in: List[int] = list(map(int,filter(lambda l: l.isnumeric() ,data_in)))

# print(string_in, len(string_in), numbers_in, sum(numbers_in))

nums_gen = (x for x in numbers_in)

string_out: str = str()

while True:
    try:
        for _ in range(next(nums_gen)):
            string_out += string_in.pop(0)
        for _ in range(next(nums_gen)):
            string_in.pop(0)
    except StopIteration as _:
        break
    except IndexError as _:
        break

print(string_out)