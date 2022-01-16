from cmath import exp


expenses: float = float()

lost_fights_count: int = int(input()) + 1
helmet_price: float = float(input())
sword_price: float = float(input())
shield_price: float = float(input())
armor_price: float = float(input())

for f in range(1, lost_fights_count):
    if f % 2 == 0:
        expenses += helmet_price

    if f % 3 == 0:
        expenses += sword_price

    if f % 6 == 0:
        expenses += shield_price
    
    if f % 12 == 0:
        expenses += armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
