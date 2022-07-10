from typing import List, ClassVar


class Vet:
    animals: ClassVar[List[str]] = list()
    space: ClassVar[int] = 5

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.animals: List[str] = list()

    def _space_in_clinic(self) -> int:
        return type(self).space - len(type(self).animals)

    def _clinic_has_free_space(self) -> bool:
        return self._space_in_clinic() > 0

    def register_animal(self, animal_name: str) -> str:
        if self._clinic_has_free_space():
            self.animals.append(animal_name)
            type(self).animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            type(self).animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {self._space_in_clinic()} space left in clinic"
