def subtract(a: int, b: int) -> int:
    return a - b

def sum_numbers(a: int, b: int) -> int:
    return a + b

def add_and_subtract(a: int, b: int, c: int) -> int:
    return subtract(sum_numbers(a, b), c)

print(add_and_subtract(int(input()), int(input()), int(input())))
