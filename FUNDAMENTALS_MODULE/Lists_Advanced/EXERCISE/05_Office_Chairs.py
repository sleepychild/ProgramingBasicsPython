from typing import List, Tuple, Generator

# inputs: Tuple[Tuple[str]] = (
#     (
#         '4',
#         'XXXX 4',
#         'XX 1',
#         'XXXXXX 3',
#         'XXX 3',
#     ),
#     (
#         '3',
#         'XXXXXXX 5',
#         'XXXX 5',
#         'XXXXXX 8',
#     ),
# )


class RoomClass:
    def __init__(self, room_num: int, definition: str) -> None:
        chairs_def, visitors_def = definition.split(' ')
        self.room_num: int = room_num
        self.chairs: int = len(chairs_def)
        self.visitors: int = int(visitors_def)
        self.free_chairs: int = self.chairs - self.visitors
        self.has_free_chairs: bool = True if self.free_chairs >= 0 else False

    def __int__(self) -> int:
        return self.free_chairs

    def __str__(self) -> str:
        if self.free_chairs >= 0:
            return f'{self.free_chairs} free in room {self.room_num}'
        else:
            return f'{abs(self.free_chairs)} more chairs needed in room {self.room_num}'


# for input_lines in inputs:
#     print(f'RUN: {input_lines}')
#     line_gen: Generator[str, None, None] = (l for l in input_lines)

#     rooms: List[RoomClass] = list()

#     for i in range(1, 1+int(next(line_gen))):
#         rooms.append(RoomClass(i, next(line_gen)))

#     rooms_without_enough_chairs: List[RoomClass] = list(
#         filter(lambda r: not r.has_free_chairs, rooms))

#     if len(rooms_without_enough_chairs) == 0:
#         print(
#             f'Game On, {sum(room.free_chairs for room in list(filter(lambda r: r.has_free_chairs, rooms)))} free chairs left')
#     else:
#         for room in rooms_without_enough_chairs:
#             print(room)

rooms: List[RoomClass] = list()

for i in range(1, 1+int(input())):
    rooms.append(RoomClass(i, input()))

rooms_without_enough_chairs: List[RoomClass] = list(
    filter(lambda r: not r.has_free_chairs, rooms))

if len(rooms_without_enough_chairs) == 0:
    print(
        f'Game On, {sum(room.free_chairs for room in list(filter(lambda r: r.has_free_chairs, rooms)))} free chairs left')
else:
    for room in rooms_without_enough_chairs:
        print(room)
