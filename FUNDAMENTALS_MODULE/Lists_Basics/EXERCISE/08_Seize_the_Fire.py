from typing import Tuple, List

FireType: Tuple[str] = ('High', 'Medium', 'Low',)
FireHigh: Tuple[int] = (125, 80, 50,)
FireLow: Tuple[int] = (81, 51, 1)

class FireCell:
    def __init__(self, fire_type_in: str, fire_level_in: int) -> None:
        self.fire_type: str = fire_type_in
        self.fire_level: int = int(fire_level_in)
        fire_type_index: int = FireType.index(self.fire_type)
        self.cell_valid: bool = FireHigh[fire_type_index] >= self.fire_level >= FireLow[fire_type_index]

class Kindling:    
    def __init__(self, data_in: str, water_in: int) -> None:
        self.cells: List[FireCell] = list()
        for cell_data in data_in.split('#'):
            self.cells.append(FireCell(*cell_data.split(' = ')))
        self.water: int = water_in
        print(self)

    def __str__(self) -> str:
        water_trac: int = self.water
        fire_trac: int = int()
        effort_trac: float = float()
        string_data: str = str()
        string_data += 'Cells:\n'
        for cell in self.cells:
            if cell.cell_valid and cell.fire_level <= water_trac:
                water_trac -= cell.fire_level
                fire_trac += cell.fire_level
                effort_trac += cell.fire_level * .25
                string_data += f' - {cell.fire_level}\n'
        string_data += f'Effort: {effort_trac:.2f}\n'
        string_data += f'Total Fire: {fire_trac}'
        return string_data
        

# Kindling(input(), int(input()))
Kindling('High = 89#Low = 28#Medium = 77#Low = 23', 1250)
Kindling('High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77', 220)
