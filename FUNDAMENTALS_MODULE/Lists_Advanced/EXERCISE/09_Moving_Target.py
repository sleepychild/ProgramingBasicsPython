from typing import Generator, List, Tuple, Callable

test_runs: Tuple[Tuple[str]] = (
    (
        '52 74 23 44 96 110',
        'Shoot 5 10',
        'Shoot 1 80',
        'Strike 2 1',
        'Add 22 3',
        'End',
    ),
    (
        '47 55 85 78 99 20',
        'Shoot 1 55',
        'Shoot 8 15',
        'Strike 2 3',
        'Add 0 22',
        'Add 2 40',
        'Add 2 50',
        'End',
    ),
)

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)
    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

class InvalidPlacement(Exception):
    def __str__(self) -> str:
        return 'Invalid placement!'

class StrikeMissed(Exception):
    def __str__(self) -> str:
        return 'Strike missed!'

class RangeTargets:

    def __init__(self, target_list: List[int]) -> None:
        self.target_list: List[int] = target_list

    def shoot(self, target: int, power: int) -> None:
        try:
            self.target_list[target] -= power
        except IndexError:
            return

        if self.target_list[target] <= 0:
            self.target_list.pop(target)

    def add(self, target: int, value: int) -> None:
        try:
            self._validate_add(target)
        except InvalidPlacement as e:
            print(e)
        else:
            self.target_list.insert(target, value)

    def _validate_add(self, target) -> None:
        if not 0 <= target < len(self.target_list):
            raise InvalidPlacement()

    def strike(self, target: int, radius: int) -> None:
        try:
            pop, count = self._validate_strike(target, radius)
        except StrikeMissed as e:
            print(e)
        else:
            for _ in range(count):
                self.target_list.pop(pop)

    def _validate_strike(self, target: int, radius: int) -> Tuple[int]:
        start: int = target - radius
        end: int = target + radius
        if start < 0 or end >= len(self.target_list):
            raise StrikeMissed()
        else:
            return start, ( radius * 2 ) + 1

    def __str__(self) -> str:
        return '|'.join([ str(x) for x in self.target_list ])

    @classmethod
    def FromString(cls, targets_data: str) -> 'RangeTargets':
        return cls([ int(x) for x in targets_data.split(' ') ])

def solution():
    range_targets: RangeTargets = RangeTargets.FromString(input())

    while True:
        command_in: str = input().split(' ')
        
        print(command_in)
        
        if command_in[0] == 'End':
            break
        elif command_in[0] == 'Shoot':
            range_targets.shoot(int(command_in[1]), int(command_in[2]))
        elif command_in[0] == 'Add':
            range_targets.add(int(command_in[1]), int(command_in[2]))
        elif command_in[0] == 'Strike':
            range_targets.strike(int(command_in[1]), int(command_in[2]))

    print(range_targets)

# solution()

for test_run in test_runs:
    input: Callable[[], str] = get_run_generator(test_run)
    solution()
