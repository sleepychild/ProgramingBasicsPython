class Flower:
    def __init__(self, name: str, water_requirements: int) -> None:
        self.name: str = name
        self.water_requirements: int = water_requirements
        self.is_happy: bool = bool()

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is{'' if self.is_happy else ' not'} happy"
