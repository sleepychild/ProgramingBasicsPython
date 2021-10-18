student_name: str = input()
grades: list = list()
grade: float
year: int = 1
failed: int = 0

while True:
    grade = float(input())
    if grade < 4:
        failed += 1
        if failed > 1:
            print(f'{student_name} has been excluded at {year} grade')
            exit(0)
    else:
        failed = 0
        year += 1
        grades.append(grade)
        if year > 12:
            print(f'{student_name} graduated. Average grade: {sum(grades) / len(grades):.2f}')
            exit(0)
