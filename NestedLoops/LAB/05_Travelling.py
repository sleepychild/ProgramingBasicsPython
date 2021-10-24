destination: str = str()
cost: float = float()

while True:
    destination = input()
    if destination == 'End':
        exit(0)
    cost = float(input())
    while cost > 0:
        cost -= float(input())
    print(f'Going to {destination}!')
