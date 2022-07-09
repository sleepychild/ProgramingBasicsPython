from typing import Union


class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name: str = name
        self.health: int = health

    def heal(self, amount: int) -> None:
        self.health += amount

    def defend(self, damage: int) -> Union[None, str]:
        self.health = max([self.health - damage, 0])
        if self.health == 0:
            return f"{self.name} was defeated"
        else:
            return
