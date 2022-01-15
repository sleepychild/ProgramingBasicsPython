cake_pieces: int = int(input()) * int(input())
input_data: str = str()

while True:
    input_data = input()

    if input_data == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        exit(0)

    cake_pieces -= int(input_data)

    if cake_pieces < 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        exit(0)
