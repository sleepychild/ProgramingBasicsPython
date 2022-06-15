def recursive_power(number, power):
    return number * recursive_power(number, power - 1) if power > 1 else number


print(recursive_power(2, 10))
print(recursive_power(10, 100))
