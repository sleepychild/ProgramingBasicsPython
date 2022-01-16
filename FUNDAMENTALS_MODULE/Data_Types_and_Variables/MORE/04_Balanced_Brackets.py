balanced: bool = True
opened: bool = False
line_in: str = str()

for _ in range(int(input())):
    line_in = input()
    if line_in == '(':
        if not opened:
            opened = True
        else:
            balanced = False
    elif line_in == ')':
        if opened:
            opened = False
        else:
            balanced = False

print('BALANCED' if balanced else 'UNBALANCED')
