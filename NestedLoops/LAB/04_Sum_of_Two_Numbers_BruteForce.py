a: int = int(input())
b: int = int(input())
m: int = int(input())

c_count: int = int()

for x in range(a, b+1):
    for y in range(a, b+1):
        c_count += 1
        if (x + y) == m:
            print(f'Combination N:{c_count} ({x} + {y} = {m})')
            exit(0)

print(f'{c_count} combinations - neither equals {m}')
