from typing import List, Tuple

from .jockey import Jockey


class HorseRace:
    RACE_TYPES: Tuple[str] = (
        "Winter",
        "Spring",
        "Autumn",
        "Summer",
    )

    def __init__(self, race_type: str) -> None:
        self.race_type: str = race_type
        self.jockeys: List[Jockey] = list()

    @property
    def race_type(self) -> str:
        return self.__race_type

    @race_type.setter
    def race_type(self, new_race_type: str) -> None:
        if new_race_type in self.RACE_TYPES:
            self.__race_type: str = new_race_type
        else:
            raise ValueError("Race type does not exist!")
