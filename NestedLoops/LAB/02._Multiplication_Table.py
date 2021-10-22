a: int = 1
b: int = 1

while a <= 10:
    while b <= 10:
        print(f'{a} * {b} = {a*b}')
        b += 1
    b = 1
    a += 1
