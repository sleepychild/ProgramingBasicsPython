cups_of_joe: int = int()
events: tuple = ('coding', 'movie', 'dog', 'cat',)
event: str = str()
while True:
    event = input()
    if event == 'END':
        break
    elif event.lower() in events:
        cups_of_joe += 2 if event.isupper() else 1
print('You need extra sleep' if cups_of_joe > 5 else cups_of_joe )
