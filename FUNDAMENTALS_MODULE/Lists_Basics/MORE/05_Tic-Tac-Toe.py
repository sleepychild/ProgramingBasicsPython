from typing import List, Tuple

play_field: List[List[int]] = [
    [ int(x) for x in input().split(' ') ],
    [ int(x) for x in input().split(' ') ],
    [ int(x) for x in input().split(' ') ],
    ]

# play_field: List[List[int]] = [
#     [ int(x) for x in '2 0 1'.split(' ') ],
#     [ int(x) for x in '0 1 0'.split(' ') ],
#     [ int(x) for x in '1 0 2'.split(' ') ],
#     ] # First player won

# play_field: List[List[int]] = [
#     [ int(x) for x in '0 1 0'.split(' ') ],
#     [ int(x) for x in '2 2 2'.split(' ') ],
#     [ int(x) for x in '1 0 0'.split(' ') ],
#     ] # Second player won

# play_field: List[List[int]] = [
#     [ int(x) for x in '1 0 2'.split(' ') ],
#     [ int(x) for x in '0 1 2'.split(' ') ],
#     [ int(x) for x in '1 2 0'.split(' ') ],
#     ] # Draw!

FRW: Tuple[int] = (1,0,)
DWN: Tuple[int] = (0,1,)
DFD: Tuple[int] = (1,1,)
DFU: Tuple[int] = (1,-1,)

PTL: Tuple[int] = (0,0,)
PTM: Tuple[int] = (1,0,)
PTR: Tuple[int] = (2,0,)

PLM: Tuple[int] = (0,1,)
PLB: Tuple[int] = (0,2,)

POSITIONS: List[Tuple[int]] = [PTL, PTM, PTR, PLM, PLB]
DIRECTIONS: List[Tuple[int]] = [FRW, DWN, DFD, DFU]


class IntVec2D:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Checker:
    def __init__(self) -> None:
        self.pos: IntVec2D = IntVec2D(0,0)
    
    def translate(self, translation_vector: IntVec2D) -> None:
        self.pos.x += translation_vector.x
        self.pos.y += translation_vector.y

    def check(self, start: IntVec2D, direction: IntVec2D, play_field: List[List[int]]) -> int:
        self.pos = start
        
        element_list: List[int] = list()
        checking: bool = True

        while checking:
            try:
                element_list.append(play_field[self.pos.y][self.pos.x])
            except:
                checking = False
            else:
                self.translate(direction)
        
        return element_list[0] if element_list.count(element_list[0]) == 3 else -1


chkr: Checker = Checker()

for position in POSITIONS:
    for direction in DIRECTIONS:
        result: int = chkr.check(IntVec2D(*position), IntVec2D(*direction), play_field)
        if result > 0:
            print(f'{"First" if result == 1 else "Second"} player won')
            exit(0)

print("Draw!")
