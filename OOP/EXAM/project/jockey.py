from typing import Union
from project.horse_specification.horse import Horse


class Jockey:
    MIN_AGE: int = 18

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.horse: Union[Horse, None] = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if new_name.strip() == "":
            raise ValueError("Name should contain at least one character!")
        else:
            self.__name: str = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < self.MIN_AGE:
            raise ValueError("Jockey myst be at least 18 to participate in the race!")
        else:
            self.__age: int = new_age
