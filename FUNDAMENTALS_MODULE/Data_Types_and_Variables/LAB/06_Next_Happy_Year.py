def increment(i: int, nl: list) -> None:
    if nl[i] == 9 and i > 0:
        nl[i] = 0
        increment(i-1, nl)
    else:
        nl[i] += 1

def check(nl: list) -> bool:
    for n in nl:
        if nl.count(n) != 1:
            return False
    return True

numbers_list: list = list()

for d in list(input()):
    numbers_list.append(int(d))

increment(len(numbers_list) - 1, numbers_list)

while not check(numbers_list):
    increment(len(numbers_list) - 1, numbers_list)

for d in numbers_list:
    print(d, end='')
