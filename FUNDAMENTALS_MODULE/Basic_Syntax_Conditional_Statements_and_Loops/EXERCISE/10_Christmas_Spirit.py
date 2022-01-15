quantity: int = int(input())
days: int = int(input())

ornament_set: int = 2
tree_skirt: int = 5
tree_garlands: int = 3
tree_lights: int = 15

budget: int = int()
totalSpirit: int = int()

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        totalSpirit += 5
        budget += ornament_set * quantity

    if day % 3 == 0:
        totalSpirit += 13
        budget += ( tree_skirt + tree_garlands ) * quantity
    
    if day % 5 == 0:
        totalSpirit += 17
        budget += tree_lights * quantity

    if day % 10 == 0:
        totalSpirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights

    if day % 15 == 0:
        totalSpirit += 30

if days % 10 == 0:
    totalSpirit -= 30

print(f'Total cost: {budget}\nTotal spirit: {totalSpirit}')