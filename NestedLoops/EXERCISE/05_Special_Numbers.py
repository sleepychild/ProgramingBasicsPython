number: int = int(input())
dividers: list = list()

for divider in range(1, 10):
    if not number % divider:
        dividers.append(divider)

output_str: str = str()

for a in dividers:
    for b in dividers:
        for c in dividers:
            for d in dividers:
                output_str += f'{a}{b}{c}{d} '

print(output_str)
