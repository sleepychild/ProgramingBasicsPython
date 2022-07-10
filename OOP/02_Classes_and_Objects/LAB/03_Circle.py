from typing import ClassVar


class Circle:
    pi: ClassVar[float] = 3.14

    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def set_radius(self, new_radius: float) -> None:
        self.radius: float = new_radius

    def get_area(self) -> None:
        return self.pi * self.radius**2

    def get_circumference(self) -> None:
        return 2 * self.pi * self.radius
