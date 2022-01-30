from typing import List

gifts: List[str] = input().split(' ')

while True:
    command: str = input()

    if command == 'No Money':
        print(' '.join(list(filter(lambda el: el != "None",gifts))))
        exit(0)
    else:
        parts: List[str] = command.split(' ')
        com_name = parts[0]
        com_gift = parts[1]
    
    if com_name == 'OutOfStock':
        gifts_new: List[str] = list()
        for gift in gifts:
            if gift == com_gift:
                gifts_new.append('None')
            else:
                gifts_new.append(gift)
        gifts = gifts_new.copy()
    elif com_name == 'Required':
        com_index = int(parts[2])
        if com_index in range(len(gifts)):
            gifts[com_index] = com_gift
    elif com_name == 'JustInCase':
        gifts[-1] = com_gift
