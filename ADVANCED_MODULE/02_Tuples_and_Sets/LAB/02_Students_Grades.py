from collections import deque
from typing import Deque, Generator, Callable, Tuple, List, Dict


DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        "7",
        "Peter 5.20",
        "Mark 5.50",
        "Peter 3.20",
        "Mark 2.50",
        "Alex 2.00",
        "Mark 3.46",
        "Alex 3.00",
    ),
    (
        "4",
        "Scott 4.50",
        "Ted 3.00",
        "Scott 5.00",
        "Ted 3.66",
    ),
    (
        "5",
        "Lee 6.00",
        "Lee 5.50",
        "Lee 6.00",
        "Peter 4.40",
        "Kenny 3.30",
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)

    return generate_input


def solution() -> None:
    students: Dict[str, List] = dict()
    for _ in range(int(input())):
        student_name, student_grade = input().split()
        if not student_name in students:
            students[student_name] = list()
        students[student_name].append(float(student_grade))

    for student_name, student_grades in students.items():
        print(
            f"{student_name} -> {' '.join([ '{:.2f}'.format(grade) for grade in student_grades ])} (avg: {sum(student_grades)/len(student_grades):.2f})"
        )


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
