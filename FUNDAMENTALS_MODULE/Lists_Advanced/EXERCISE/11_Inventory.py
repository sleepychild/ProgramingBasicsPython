from typing import Generator, List, Tuple, Callable

test_runs: Tuple[Tuple[str]] = (
    (
        'Iron, Wood, Sword',
        'Collect - Gold',
        'Drop - Wood',
        'Craft!',
    ),
    (
        'Iron, Sword',
        'Drop - Bronze',
        'Combine Items - Sword:Bow',
        'Renew - Iron',
        'Craft!',
    ),
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)
    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

class InventoryClass:

    def __init__(self, items: List[str]) -> None:
        self.items: List[str] = items

    def collect(self, arg: str) -> None:
        if not arg in self.items:
            self.items.append(arg)
    
    def drop(self, arg: str) -> None:
        try:
            self.items.remove(arg)
        except ValueError as _:
            pass

    def combine_items(self, arg: str) -> None:
        old_item, new_item = arg.split(':')
        try:
            old_item_index: int = self.items.index(old_item)
        except ValueError as _:
            pass
        else:
            self.items.insert(old_item_index+1, new_item)
    
    def renew(self, arg: str) -> None:
        try:
            self.items.remove(arg)
        except ValueError as _:
            pass
        else:
            self.items.append(arg)

    def run(self) -> None:
        while True:
            instruction: str = input()
            if instruction == 'Craft!':
                break
            else:
                cmd, arg = instruction.split(' - ')
                self.__getattribute__(cmd.replace(' ','_').lower())(arg)
        print(self)
    
    def __str__(self) -> str:
        return ', '.join(self.items)

    @classmethod
    def FromString(cls, items: str) -> 'InventoryClass':
        return cls(items.split(', '))

def solution():
    inventory: InventoryClass = InventoryClass.FromString(input())
    inventory.run()

solution()

# for test_run in test_runs:
#     input: Callable[[], str] = get_run_generator(test_run)
#     solution()
