seasons: tuple = ('Spring', 'Summer', 'Autumn', 'Winter',)
boat_rates: tuple = (3000, 4200, 4200, 2600)

budget: int = int(input())
season: str = input()
people: int = int(input())

expenses: float = boat_rates[seasons.index(season)]
expenses *= .75 if people >= 12 else .85 if people > 6 else .9
expenses *= .95 if (people % 2) == 0 and season != 'Autumn' else 1

budget -= expenses

if budget < 0:
    print(f'Not enough money! You need {abs(budget):.2f} leva.')
else:
    print(f'Yes! You have {budget:.2f} leva left.')
