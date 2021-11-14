a_max: int = int(input()) + 1
b_max: int = int(input()) + 1
c_max: int = int(input()) + 1

for a in range(2, a_max):
    if a % 2 == 0:
        for b in range(2, b_max):
            if b in [2, 3, 5, 7]:
                for c in range(2, c_max):
                    if c % 2 == 0:
                        print(a, b, c)
