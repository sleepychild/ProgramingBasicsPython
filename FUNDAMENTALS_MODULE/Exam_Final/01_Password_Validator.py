from typing import List, Tuple, Generator, Callable
import string

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'invalidpassword*',
        'Add 2 p',
        'Replace i -50',
        'Replace * 10',
        'Make Upper 2',
        'Validation',
        'Complete',
    ),
    (
        '123456789',
        'Insert 3 R',
        'Replace 5 15',
        'Validation',
        'Make Lower 3',
        'Complete',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input

acceptable: str = string.ascii_uppercase+string.ascii_lowercase+string.digits+"_"
if DEBUG:
    print(acceptable)

def solution():
    initial_password: List[str] = list(input())
    while True:
        lin: str = input()
        if lin == 'Complete':
            break
        lin_parts: List[str] = lin.split()
        command: str = lin_parts[0]
        if command == 'Make':
            op_to: str = lin_parts[1]
            index: int = int(lin_parts[2])
            if op_to == 'Upper':
                initial_password[index] = initial_password[index].upper()
            elif op_to == 'Lower':
                initial_password[index] = initial_password[index].lower()
            print(''.join(initial_password))
        elif command == 'Insert':
            index: int = int(lin_parts[1])
            char: str = lin_parts[2]
            if index in range(len(initial_password)):
                initial_password.insert(index, char)
                print(''.join(initial_password))
        elif command == 'Replace' and lin_parts[1] in initial_password:
            char: str = lin_parts[1]
            value: int = int(lin_parts[2])
            new_char: str = chr(ord(char)+value)
            while char in initial_password:
                initial_password[initial_password.index(char)] = new_char
            print(''.join(initial_password))
        elif command == 'Validation':
            if len(initial_password) < 8:
                print('Password must be at least 8 characters long!')
            has_invalid: bool = False
            has_upper: bool = False
            has_lower: bool = False
            has_digit: bool = False
            for char in initial_password:
                if char not in acceptable:
                    has_invalid = True
                if char in string.ascii_uppercase:
                    has_upper = True
                if char in string.ascii_lowercase:
                    has_lower = True
                if char in string.digits:
                    has_digit = True
            if has_invalid:
                print("Password must consist only of letters, digits and _!")
            if not has_upper:
                print("Password must consist at least one uppercase letter!")
            if not has_lower:
                print("Password must consist at least one lowercase letter!")
            if not has_digit:
                print("Password must consist at least one digit!")

if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
