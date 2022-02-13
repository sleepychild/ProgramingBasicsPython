from typing import Generator, List, Tuple, Callable

test_runs: Tuple[Tuple[str]] = (
    (
        '2, 3, 5, 15, 75',
        '5',
    ),
    (
        '2, 3, 5, 15, 75',
        '20',
    ),(
        '2, 3, 5, 45, 45',
        '30',
    ),
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)
    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

class GenericListClass:
    
    def __init__(self, items: List, items_type: type) -> None:
        self.items: List[items_type] = items
        self.items_type: type = items_type

    def fucking_desgusting_comunism(self) -> None:
        immoral_handouts: int = int(input())
        sum_elements: int = sum(self.items)
        num_elements: int = len(self.items)
        if sum_elements / num_elements < immoral_handouts:
            print('No equal distribution possible')
            return
        else:
            while 0 != len(list(filter(lambda x: x < immoral_handouts, self.items))):
                max_val: int = max(self.items)
                max_ind: int = self.items.index(max_val)
                min_val: int = min(self.items)
                min_ind: int = self.items.index(min_val)
                theft: int = immoral_handouts - min_val
                self.items[max_ind] -= theft
                self.items[min_ind] += theft
            print(self.items)

    def __str__(self) -> str:
        return str(self.items)
        # try:
        #     return ' '.join(self.items)
        # except TypeError:
        #     return ' '.join([ str(item) for item in self.items ])

    @classmethod
    def FromString(cls, input_str: str, separator: str, type_wanted: type) -> 'GenericListClass':
        return cls([ type_wanted(x) for x in input_str.split(separator) ], type_wanted)

def solution():
    list_object: GenericListClass = GenericListClass.FromString(input(), ', ', int)
    list_object.fucking_desgusting_comunism()

solution()

# for test_run in test_runs:
#     input: Callable[[], str] = get_run_generator(test_run)
#     solution()
