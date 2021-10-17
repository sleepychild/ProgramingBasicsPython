fails_threshold: int = int(input())
fails_count: int = int()

last_problem: str = str()

grades: list = list()
grade: float = float()

input_str: str = str()

while True:
    input_str = input()

    if input_str == 'Enough':
        print(f'Average score: {sum(grades) / len(grades):.2f}')
        print(f'Number of problems: {len(grades)}')
        print(f'Last problem: {last_problem}')
        exit(0)

    last_problem = input_str
    grade = float(input())
    grades.append(grade)
    fails_count += 0 if grade > 4 else 1

    if fails_count == fails_threshold:
        print(f'You need a break, {fails_threshold} poor grades.')
        exit(0)
