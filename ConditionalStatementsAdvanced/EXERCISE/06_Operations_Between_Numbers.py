def addsubmul(n1, n2, op):
    res: float = eval(f'{n1} {op} {n2}')
    print(f'{n1} {op} {n2} = {res} - {"even" if (res % 2) == 0 else "odd"}')


def division(n1, n2, op):
    try:
        res: float = eval(f'{n1} {op} {n2}')
    except ZeroDivisionError as e:
        print(f'Cannot divide {n1} by zero')
    else:
        if op == '/':
            print(f'{n1} {op} {n2} = {res:.2f}')
        else:
            print(f'{n1} {op} {n2} = {res}')


calculator: dict = {
    '+': addsubmul,
    '-': addsubmul,
    '*': addsubmul,
    '/': division,
    '%': division,
}

num1: int = int(input())
num2: int = int(input())
operator: str = input()

calculator[operator](num1, num2, operator)
