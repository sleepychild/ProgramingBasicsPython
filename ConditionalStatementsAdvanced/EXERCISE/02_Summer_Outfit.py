temp: int = int(input())
temp_range: int = 0 if (10 <= temp <= 18) else 1 if (18 < temp <= 24) else 2
day_time: int = ('Morning', 'Afternoon', 'Evening',).index(input())
options: tuple = (
    (('Sweatshirt', 'Sneakers',),('Shirt','Moccasins',),('Shirt','Moccasins',),),
    (('Shirt','Moccasins',),('T-Shirt','Sandals',),('Shirt','Moccasins',),),
    (('T-Shirt','Sandals',),('Swim Suit','Barefoot',),('Shirt','Moccasins',),),
)
print(f'It\'s {temp} degrees, get your {options[temp_range][day_time][0]} and {options[temp_range][day_time][1]}.')
