from typing import ClassVar


class Glass:
    capacity: ClassVar[int] = 250

    def __init__(self) -> None:
        self.content: int = int()

    def fill(self, ml: int) -> str:
        if (self.capacity - self.content) >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = int()
        return "Glass is now empty"

    def info(self) -> str:
        return f"{self.capacity - self.content} ml left"
