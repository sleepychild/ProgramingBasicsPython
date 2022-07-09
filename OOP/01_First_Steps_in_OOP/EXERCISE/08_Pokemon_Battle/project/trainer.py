from typing import List
from .pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.pokemons: List[Pokemon] = list()

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            self.pokemons.remove(
                next(filter(lambda p: p.name == pokemon_name, self.pokemons))
            )
        except StopIteration as _:
            return f"Pokemon is not caught"
        else:
            return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        return_data: str = (
            f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        )
        for pokemon in self.pokemons:
            return_data += f"- {pokemon.pokemon_details()}\n"
        return return_data
