animals_list: list = input().split(', ')
animals_list.reverse()
for i in range(len(animals_list)):
    if animals_list[i] == 'wolf':
        if i == 0:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
