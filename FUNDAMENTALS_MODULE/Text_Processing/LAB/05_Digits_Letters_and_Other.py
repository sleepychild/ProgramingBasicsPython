lin: str = input()

# v1

d: str = str()
l: str = str()
o: str = str()

for c in lin:
    if c.isdigit():
        d += c
    elif c.isalpha():
        l += c
    else:
        o += c

print(d)
print(l)
print(o)

# v2

print(''.join([c for c in lin if c.isdigit()]))
print(''.join([c for c in lin if c.isalpha()]))
print(''.join([c for c in lin if not (c.isdigit() or c.isalpha())]))
