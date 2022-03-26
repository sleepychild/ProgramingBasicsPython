ns, hs = input(), input()

for n in ns.split(', '):
    while n in hs:
        hs = hs.replace(n, '*'*len(n))

print(hs)
