from typing import List, Callable

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
        count: int = int(args[0])
        num_type: Callable[[int], bool] = self.__getattribute__(f'_{args[1]}')
        try:
            self._count_check(count)
        except InvalidCount as e:
            print(e)
        else:
            print(list(filter(num_type, self))[:count])

    def last(self, *args) -> None:
        count: int = int(args[0])
        num_type: Callable[[int], bool] = self.__getattribute__(f'_{args[1]}')
        try:
            self._count_check(count)
        except InvalidCount as e:
            print(e)
        else:
            print(list(filter(num_type, self))[-count:])

    def _count_check(self, count: int) -> None:
        if count > self.length :
            raise InvalidCount

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


if __name__ == '__main__':
    interlist: InteractiveList = InteractiveList.list_from_string(input(), ' ', int)
    while True:
        cmd_prt: List[str] = input().split(' ')
        interlist.__getattribute__(cmd_prt[0])(*cmd_prt[1:])
