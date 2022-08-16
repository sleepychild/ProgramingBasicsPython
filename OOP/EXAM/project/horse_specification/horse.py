from abc import ABC, abstractmethod


class Horse(ABC):
    MAXIMUM_SPEED: int = int()
    TRAIN_INCREASE: int = int()

    @abstractmethod
    def __init__(self, name: str, speed: int) -> None:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name.strip()) < 4:
            raise ValueError(f"Horse name {new_name} is less than 4 symbols!")
        else:
            self.__name: str = new_name

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        if new_speed > self.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")
        else:
            self.__speed: int = new_speed

    @property
    def is_taken(self) -> bool:
        return self.__is_taken

    @is_taken.setter
    def is_taken(self, new_is_taken) -> None:
        self.__is_taken: bool = new_is_taken

    def train(self) -> None:
        try:
            self.speed += self.TRAIN_INCREASE
        except ValueError as _:
            self.speed: int = self.MAXIMUM_SPEED
