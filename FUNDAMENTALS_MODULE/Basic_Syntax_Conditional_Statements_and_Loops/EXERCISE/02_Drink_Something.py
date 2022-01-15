age: int = int(input())
drinks: tuple = ('toddy', 'coke', 'beer', 'whisky',)
drink_index: int = 0 if age <= 14 else 1 if age <= 18 else 2 if age <= 21 else 3
print(f'drink {drinks[drink_index]}')
