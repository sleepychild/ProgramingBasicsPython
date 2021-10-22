hour: int = int()
minute: int = int()

while hour < 24:
    while minute < 60:
        print(f'{hour}:{minute}')
        minute += 1
    minute = 0
    hour += 1
