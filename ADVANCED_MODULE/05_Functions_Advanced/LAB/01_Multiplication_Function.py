def multiply(*args) -> int:
    result: int = args[0]
    for arg in args[1:]:
        result *= arg
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
