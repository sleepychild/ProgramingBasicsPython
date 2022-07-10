from typing import List


class Vehicle:
    def __init__(
        self, mileage: int, max_speed: int = 150, gadgets: List[str] = list()
    ) -> None:
        self.mileage: int = mileage
        self.max_speed: int = max_speed
        self.gadgets: List[str] = gadgets
