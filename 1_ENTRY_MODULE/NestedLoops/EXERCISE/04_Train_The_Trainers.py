trainers_count: int = int(input())

input_data: str = str()

course_name: str = str()
course_grades: list = list()
courses_avgs: list = list()
final_avg: float = float()

output_data: str = str()

while True:
    input_data = input()
    if input_data == 'Finish':
        break
    course_name = input_data
    course_grades = list()
    for _ in range(trainers_count):
        course_grades.append(float(input()))
    courses_avgs.append( sum(course_grades) / len(course_grades) )
    output_data += f'{course_name} - {courses_avgs[-1]:.2f}.\n'

output_data += f'Student\'s final assessment is { sum(courses_avgs) / len(courses_avgs) :.2f}.'
print(output_data)
