target: int = 500
hit_count: int = int()
a: int = target
b: int = int()
c: int = int()

while 0 <= a <= target:
    while 0 <= b <= target:
        hit_count += 1
        b -= 1
        c += 1
    a -= 1
    b = target - a
    c = 0

print(hit_count)
