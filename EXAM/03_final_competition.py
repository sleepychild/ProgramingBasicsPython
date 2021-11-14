seasons: tuple = ('summer', 'winter')
locations: tuple = ('Bulgaria', 'Abroad')
expences: tuple = ((.95, .9),(.92, .85))

dancers: int = int(input())
points: float = float(input())

season: int = seasons.index(input())
location: int = locations.index(input())

prize: float = ( points * dancers ) if location == 0 else ( ( dancers * points ) * 1.5 )
prize_sans_expences: float = prize * expences[season][location] 

charity: float = prize_sans_expences * .75
money: float = (prize_sans_expences - charity) / dancers

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {money:.2f}')
