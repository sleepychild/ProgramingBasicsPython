from .horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED: int = 120
    TRAIN_INCREASE: int = 2

    def __init__(self, name: str, speed: int) -> None:
        self.name: str = name
        self.speed: int = speed
        self.is_taken: bool = bool()
