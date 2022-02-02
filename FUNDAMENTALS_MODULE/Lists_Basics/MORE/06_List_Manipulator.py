from typing import List

input_data: str = '1 3 5 7 9'
cmds: List[str] = [
    'exchange 1',
    'max odd',
    'min even',
    'first 2 odd',
    'last 2 even',
    'exchange 3',
    'end',
]

# input_data: str = '1 10 100 1000'
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

# input_data: str = '1 10 100 1000'
# cmds: List[str] = [
#     'exchange 3',
#     'first 2 odd',
#     'last 4 odd',
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
            for _ in range(index):
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
        exit()

    def _max_min_even_odd(self, mode, num_type) -> int:
        try:
            t_val: int = mode(filter(num_type, self))
        except ValueError as _:
            raise NoMatches
        else:
            return self.index(t_val)

    def _first_last_even_odd(self, mode: int, num_type, count: int) -> List:
        self._count_check(count)


    def _even(self, n: int) -> bool:
        return (n % 2) == 0

    def _odd(self, n: int) -> bool:
        return (n % 2) != 0

    def _index_check(self, index: int) -> None:
        if not index in range(0, len(self)) :
            raise InvalidIndex

    def _count_check(self, count: int) -> None:
        if count > len(self) :
            raise InvalidCount

    @classmethod
    def list_from_string(cls, str_in: str, str_delimiter: str, element_type: type) -> 'InteractiveList':
        return cls([ element_type(list_element) for list_element in str_in.split(str_delimiter)])

interlist: InteractiveList = InteractiveList.list_from_string(input_data, ' ', int)
print(interlist)

for command in cmds:
    command_parts: List[str] = command.split(' ')
    print(command_parts)
    interlist.__getattribute__(command_parts[0])(*command_parts[1:])
    print(interlist)
