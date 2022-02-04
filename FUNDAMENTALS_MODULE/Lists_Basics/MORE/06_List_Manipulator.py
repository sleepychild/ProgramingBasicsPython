from typing import List, Callable, Tuple

input_data: Tuple[str] = (
    '1 3 5 7 9',
    '1 10 100 1000',
    '1 10 100 1000',
)

results_data: Tuple[str] = (
    '[3, 5, 7, 9, 1]',
    '[10, 100, 1000, 1]',
    '[1, 10, 100, 1000]',
)

input_data_cmd: Tuple[Tuple[str]] = (
    (
        'exchange 1',
        'max odd',
        'min even',
        'first 2 odd',
        'last 2 even',
        'exchange 3',
        'end',
    ),(
        'max even',
        'first 5 even',
        'exchange 10',
        'min odd',
        'exchange 0',
        'max even',
        'min even',
        'end',
    ),(
        'exchange 3',
        'first 2 odd',
        'last 4 odd',
        'end',
    ),
)


class InvalidIndex(Exception):
    def __str__(self) -> str:
        return 'Invalid index'


class InvalidCount(Exception):
    def __str__(self) -> str:
        return 'Invalid count'


class NoMatches(Exception):
    def __str__(self) -> str:
        return 'No matches'


class InteractiveList(list):

    def __init__(self, list_in: List) -> None:
        super().__init__(list_in)
        self.length = len(self)

    def exchange(self, *args) -> None:
        index: int = int(args[0])
        try:
            self._index_check(index)
        except InvalidIndex as e:
            print(e)
        else:
            for _ in range(index+1):
                self.append(self.pop(0))

    def max(self, *args) -> None:
        try:
            print(self._max_min_even_odd(max, self.__getattribute__(f'_{args[0]}')))
        except NoMatches as e:
            print(e)

    def min(self, *args) -> None:
        try:
            print(self._max_min_even_odd(min, self.__getattribute__(f'_{args[0]}')))
        except NoMatches as e:
            print(e)

    def first(self, *args) -> None:
        try:
            print(self._first_last_even_odd(1, self.__getattribute__(f'_{args[1]}'), int(args[0])))
        except InvalidCount as e:
            print(e)
    
    def last(self, *args) -> None:
        try:
            print(self._first_last_even_odd(-1, self.__getattribute__(f'_{args[1]}'), int(args[0])))
        except InvalidCount as e:
            print(e)

    def end(self) -> None:
        print(self)
        exit(0)

    def _max_min_even_odd(self, mode: Callable[..., int], num_type: Callable[[int], bool]) -> int:
        try:
            t_val: int = mode(filter(num_type, self))
        except ValueError as _:
            raise NoMatches
        else:
            t_ind: int = int()
            for _ in range(self.count(t_val)):
                try:
                    t_ind = self.index(t_val, t_ind+1)
                except ValueError:
                    pass
            return t_ind

    def _first_last_even_odd(self, mode: int, num_type: Callable[[int], bool], count: int) -> List:
        if count > self.length :
            raise InvalidCount
        else:
            return list(filter(num_type, self))[::mode][:count]

    def _index_check(self, index: int) -> None:
        if not 0 <= index < self.length:
            raise InvalidIndex

    @staticmethod
    def _even(n: int) -> bool:
        return (n % 2) == 0

    @staticmethod
    def _odd(n: int) -> bool:
        return (n % 2) != 0

    @classmethod
    def list_from_string(cls, str_in: str, str_delimiter: str, element_type: type) -> 'InteractiveList':
        return cls([ element_type(list_element) for list_element in str_in.split(str_delimiter)])

# for i in range(len(input_data)):
#     interlist: InteractiveList = InteractiveList.list_from_string(input_data[i], ' ', int)
#     print(f'RUN: {i} with {interlist}')
#     for command in input_data_cmd[i]:
#         command_parts: List[str] = command.split(' ')
#         print(command_parts, end=" => ")
#         interlist.__getattribute__(command_parts[0])(*command_parts[1:])
#         print(interlist)
#     print(results_data[i])

if __name__ == '__main__':
    interlist: InteractiveList = InteractiveList.list_from_string(input(), ' ', int)
    while True:
        cmd_prt: List[str] = input().split(' ')
        interlist.__getattribute__(cmd_prt[0])(*cmd_prt[1:])

"""
Normal          V X V V V V V V X V
No exchange     X X X V X X X X X X
No max          X X X X X V X X X X
No min          X X X X X V V X X X
No first        X X X X X X X X X X
No last         X X X X X X V X X X
"""
