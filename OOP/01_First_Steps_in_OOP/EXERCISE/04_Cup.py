class Cup:
    def __init__(self, size: int, quantity: int) -> None:
        self.size: int = size
        self.quantity: int = quantity

    def status(self) -> int:
        return self.size - self.quantity

    def fill(self, quantity: int) -> None:
        self.quantity += quantity if self.status() >= quantity else 0
