def operate(op, *args):
    initial = args[0]
    for arg in args[1:]:
        initial = eval(f"{initial} {op} {arg}")
    return initial


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
