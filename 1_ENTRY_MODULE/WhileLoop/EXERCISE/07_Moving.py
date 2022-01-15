space: int = int(input()) * int(input()) * int(input())
input_data: str = str()

while True:
    input_data = input()

    if input_data == 'Done':
        print(f'{space} Cubic meters left.')
        exit(0)

    space -= int(input_data)

    if space < 0:
        print(f'No more free space! You need {abs(space)} Cubic meters more.')
        exit(0)
