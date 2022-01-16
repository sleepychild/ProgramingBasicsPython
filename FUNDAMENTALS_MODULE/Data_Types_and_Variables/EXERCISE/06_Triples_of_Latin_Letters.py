chars: list = list()

for c in range(97, 97 + int(input())):
    chars.append(chr(c))

for x in chars:
    for y in chars:
        for z in chars:
            print(x+y+z)
