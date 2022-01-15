budget: float = float(input())
flour_price: float = float(input())
eggs_price: float = flour_price * .75
milk_price: float = (flour_price * 1.25) / 4
bread_price: float = flour_price + eggs_price + milk_price

breads_made: int = int()
colored_eggs: int = int()

while budget >= bread_price:
    budget -= bread_price
    breads_made += 1
    colored_eggs += 3

    if breads_made % 3 == 0:
        colored_eggs -= breads_made - 2

print(f'You made {breads_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
