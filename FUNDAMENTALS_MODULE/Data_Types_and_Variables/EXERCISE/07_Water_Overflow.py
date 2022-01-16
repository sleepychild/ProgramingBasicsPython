capacity: int = 255
water: int = int()
inflow: int = int()

for _ in range(int(input())):
    inflow = int(input())
    if (water + inflow) > capacity:
        print('Insufficient capacity!')
    else:
        water += inflow

print(water)
