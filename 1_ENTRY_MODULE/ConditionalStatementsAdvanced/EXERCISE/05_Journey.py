seasons: tuple = (
    'summer',
    'winter',
)

expenses: tuple = (
    (.3, .7,),
    (.4, .8,),
    (.9, .9,),
)

lodging: tuple = (
    ('Camp', 'Hotel',),
    ('Camp', 'Hotel',),
    ('Hotel', 'Hotel',),
)

locations: tuple = (
    'Bulgaria',
    'Balkans',
    'Europe',
)

budget: float = float(input())
season: str = seasons.index(input())

price_tier: int = 0 if budget <= 100 else 1 if budget <= 1000 else 2

print(f'Somewhere in {locations[price_tier]}')
print(f'{lodging[price_tier][season]} - {budget * expenses[price_tier][season]:.2f}')
