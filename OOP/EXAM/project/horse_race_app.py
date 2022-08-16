from . import Jockey, HorseRace
from .horse_specification import Horse, Appaloosa, Thoroughbred
from typing import List, Dict, Union


class HorseRaceApp:
    HORSE_TYPES: Dict[str, type] = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self) -> None:
        self.horses: List[Horse] = list()
        self.jockeys: List[Jockey] = list()
        self.horce_races: List[HorseRace] = list()

    def add_horse(
        self, horse_type: str, horse_name: str, horse_speed: int
    ) -> Union[str, None]:
        try:
            new_horse_type: type = self.HORSE_TYPES[horse_type]
        except KeyError as _:
            return

        if HorseRaceApp._value_taken(horse_name, self.horses, "name"):
            raise Exception(f"Horse {horse_name} has been already added!")

        # try:
        self.horses.append(new_horse_type(horse_name, horse_speed))
        # except ValueError as _:
        #     pass
        # else:
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> Union[str, None]:
        if HorseRaceApp._value_taken(jockey_name, self.jockeys, "name"):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        # try:
        self.jockeys.append(Jockey(jockey_name, age))
        # except ValueError as _:
        #     pass
        # else:
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> Union[str, None]:
        if HorseRaceApp._value_taken(race_type, self.horce_races, "race_type"):
            raise Exception(f"Race {race_type} has been already created!")

        # try:
        self.horce_races.append(HorseRace(race_type))
        # except ValueError as _:
        #     pass
        # else:
        return f"Race {race_type} is created."

    def add_horse_to_jockey(
        self, jockey_name: str, horse_type: str
    ) -> Union[str, None]:
        if not HorseRaceApp._value_taken(jockey_name, self.jockeys, "name"):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey_index: int = HorseRaceApp._get_index(jockey_name, self.jockeys, "name")

        horse_index: int = -1

        for horse_idx, horse in enumerate(self.horses):
            if not horse.is_taken and type(horse).__name__ == horse_type:
                horse_index = horse_idx

        if horse_index == -1:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if self.jockeys[jockey_index].horse != None:
            return f"Jockey {jockey_name} already has a horse."

        self.jockeys[jockey_index].horse = self.horses[horse_index]
        self.horses[horse_index].is_taken = True
        return (
            f"Jockey {jockey_name} will ride the horse {self.horses[horse_index].name}."
        )

    def add_jockey_to_horse_race(
        self, race_type: str, jockey_name: str
    ) -> Union[str, None]:
        if not HorseRaceApp._value_taken(race_type, self.horce_races, "race_type"):
            raise Exception(f"Race {race_type} could not be found!")

        if not HorseRaceApp._value_taken(jockey_name, self.jockeys, "name"):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey_index: int = HorseRaceApp._get_index(jockey_name, self.jockeys, "name")
        horse_race_index: int = HorseRaceApp._get_index(
            race_type, self.horce_races, "race_type"
        )

        if self.jockeys[jockey_index].horse == None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if self.jockeys[jockey_index] in self.horce_races[horse_race_index].jockeys:
            return (
                f"Jockey {jockey_name} has been already added to the {race_type} race."
            )

        self.horce_races[horse_race_index].jockeys.append(self.jockeys[jockey_index])
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> Union[str, None]:
        if not HorseRaceApp._value_taken(race_type, self.horce_races, "race_type"):
            raise Exception(f"Race {race_type} could not be found!")

        horse_race_index: int = HorseRaceApp._get_index(
            race_type, self.horce_races, "race_type"
        )

        if len(self.horce_races[horse_race_index].jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed: int = int()
        jockey_name: str = str()
        horse_name: str = str()

        for jockey in self.horce_races[horse_race_index].jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."

    @staticmethod
    def _value_taken(needle: str, haystack: List, attr: str) -> bool:
        return bool(list(filter(lambda x: getattr(x, attr) == needle, haystack)))

    @staticmethod
    def _get_index(needle: str, haystack: List, attr: str) -> int:
        for index, object_instance in enumerate(haystack):
            if getattr(object_instance, attr) == needle:
                return index
