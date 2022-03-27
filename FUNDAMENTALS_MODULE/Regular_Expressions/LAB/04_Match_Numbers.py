import re

for r in re.finditer(
        r"(?P<number>(^|(?<=\s))(?P<sign>-?)(?P<whole>[0]|[1-9]\d*)(?P<decimal>\.\d+)?($|(?=\s)))", 
        input()
    ):
    print(r.group('number'), end=' ')
