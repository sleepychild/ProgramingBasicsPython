from typing import Iterator


class NumGenerator:
    target: int
    start: int
    current: int

    def __init__(self, target_in: int, start_in: int = 0) -> None:
        self.target = target_in
        self.start = start_in

    def numbers(self) -> Iterator:
        return iter(self)

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        self.current = self.current * 2 + 1

        if self.target < self.current:
            raise StopIteration

        return self.current


if __name__ == '__main__':
    num_gen = NumGenerator(int(input()))
    for i in num_gen.numbers():
        print(i)

