total: int = int()
for c in input():
    try:
        total += ('', 'a', 'e', 'i', 'o', 'u').index(c)
    except:
        pass

print(total)
