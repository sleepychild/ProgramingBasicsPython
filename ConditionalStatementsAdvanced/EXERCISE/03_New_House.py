flower_types: tuple = ('Roses', 'Dahlias', 'Tulips', 'Narcissus', 'Gladiolus',)
flower_price: tuple = (5, 3.8, 2.8, 3, 2.5)
flower_price_mod: tuple = (
    ('> 80', .9),
    ('> 90', .85),
    ('> 80', .85),
    ('< 120', 1.15),
    ('< 80', 1.2),
)

flower_type: int = flower_types.index(input())
flower_count: int = int(input())
budget: int = int(input())

flower_price_total: float = flower_price[flower_type] * flower_count
flower_price_moded: float = flower_price_total * flower_price_mod[flower_type][1]
flower_price_moded if eval(f'{flower_count} {flower_price_mod[flower_type][0]}') else flower_price_total

budget -= flower_price_moded if eval(f'{flower_count} {flower_price_mod[flower_type][0]}') else flower_price_total

if budget < 0:
    print(f'Not enough money, you need {abs(budget):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flower_count} {flower_types[flower_type]} and {budget:.2f} leva left.')
