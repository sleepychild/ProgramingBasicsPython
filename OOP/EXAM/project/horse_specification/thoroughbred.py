from .horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED: int = 140
    TRAIN_INCREASE: int = 3

    def __init__(self, name: str, speed: int) -> None:
        self.name: str = name
        self.speed: int = speed
        self.is_taken: bool = bool()
