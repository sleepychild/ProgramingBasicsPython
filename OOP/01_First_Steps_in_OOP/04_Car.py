class Car:
    def __init__(self, name: str, model: str, engine: str) -> None:
        self.name: str = name
        self.model: str = model
        self.engine: str = engine

    def get_info(self) -> str:
        return f"This is {self.name} {self.model} with engine {self.engine}"
