class Pokemon:
    def __init__(self, name: str, health: int) -> None:
        self.name: str = name
        self.health: int = health

    def pokemon_details(self) -> str:
        return f"{self.name} with health {self.health}"
