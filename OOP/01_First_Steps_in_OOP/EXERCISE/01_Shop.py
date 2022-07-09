from typing import List


class Shop:
    def __init__(self, name: str, items: List[str]) -> None:
        self.name: str = name
        self.items: List[str] = items

    def get_items_count(self) -> int:
        return len(self.items)
