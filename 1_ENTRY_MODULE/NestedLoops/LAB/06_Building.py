floors: int = int(input())
rooms_per_floor: int = int(input())

for floor in range(floors, 0, -1):
    line: str = str()
    room_type: str = 'L' if floor == floors else 'A' if floor % 2 else 'O'
    for room in range(rooms_per_floor):
        line += f'{room_type}{floor}{room} '
    print(line)
