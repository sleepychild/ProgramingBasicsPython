from typing import List, Callable

# input_data: str = '1 3 5 7 9'
input_data: str = '1 10 100 1000'

# cmds: List[str] = [
#     'exchange 1',
#     'max odd',
#     'min even',
#     'first 2 odd',
#     'last 2 even',
#     'exchange 3',
#     'end',
# ]

# cmds: List[str] = [
#     'max even',
#     'first 5 even',
#     'exchange 10',
#     'min odd',
#     'exchange 0',
#     'max even',
#     'min even',
#     'end',
# ]

cmds: List[str] = [
    'exchange 3',
    'first 2 odd',
    'last 4 odd',
    'end',
]

# input_data: str = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 100 200 500 1000 1001 2000 2001'

# cmds: List[str] = [
#     'max even',
#     'max odd',
#     'min even',
#     'min odd',
#     'first 5 even',
#     'first 5 odd',
#     'last 5 even',
#     'last 5 odd',
#     'exchange 10',
#     'max even',
#     'max odd',
#     'min even',
#     'min odd',
#     'first 5 even',
#     'first 5 odd',
#     'last 5 even',
#     'last 5 odd',
#     'exchange 40',
#     'first 40 even',
#     'end',
# ]

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

    def exchange(self, *args) -> None:
        index: int = int(args[0])
        try:
            self._index_check(index)
        except InvalidIndex as e:
            print(e)
        else:
            for _ in range(index+1):
                self.append(self.pop(0))
        # print(self)

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
        exit()

    def _max_min_even_odd(self, mode: Callable[..., int], num_type: Callable[[int], bool]) -> int:
        try:
            t_val: int = mode(filter(num_type, self))
        except ValueError as _:
            raise NoMatches
        else:
            return self.index(t_val)

    def _first_last_even_odd(self, mode: int, num_type: Callable[[int], bool], count: int) -> List:
        if count > len(self) :
            raise InvalidCount
        else:
            return list(filter(num_type, self))[::mode][:count]

    def _even(self, n: int) -> bool:
        return (n % 2) == 0

    def _odd(self, n: int) -> bool:
        return (n % 2) != 0

    def _index_check(self, index: int) -> None:
        if not 0 <= index < len(self):
            raise InvalidIndex

    @classmethod
    def list_from_string(cls, str_in: str, str_delimiter: str, element_type: type) -> 'InteractiveList':
        return cls([ element_type(list_element) for list_element in str_in.split(str_delimiter)])

interlist: InteractiveList = InteractiveList.list_from_string(input_data, ' ', int)
print(interlist)

for command in cmds:
    command_parts: List[str] = command.split(' ')
    print(command_parts, end=" => ")
    interlist.__getattribute__(command_parts[0])(*command_parts[1:])
    print(interlist)

# if __name__ == '__main__':
#     interlist: InteractiveList = InteractiveList.list_from_string(input(), ' ', int)
#     while True:
#         cmd_prt: List[str] = input().split(' ')
#         interlist.__getattribute__(cmd_prt[0])(*cmd_prt[1:])
