class Circle:
    __pi: float = 3.14

    def __init__(self, diameter: float) -> None:
        self.diameter = diameter
        self.radius = diameter/2

    def calculate_circumference(self) -> float:
        return 2 * self.__pi * self.radius

    def calculate_area(self) -> float:
        return self.__pi * (self.radius**2)

    def calculate_area_of_sector(self, angle: float) -> float:
        area: float = self.calculate_area()
        return (area/360) * angle
