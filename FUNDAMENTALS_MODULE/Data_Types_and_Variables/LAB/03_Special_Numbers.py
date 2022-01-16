special_sums: tuple = (5, 7, 11,)

n: int = int(input())

def check_special(i: int) -> bool:
    sum_i: int = int()
    for n in list(str(i)):
        sum_i += int(n)
    return sum_i in special_sums

for i in range(1, n+1):
    print(f'{i} -> {check_special(i)}')
