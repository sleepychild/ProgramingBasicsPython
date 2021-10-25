trainers_count: int = int(input())

input_data: str = str()

course_name: str = str()
course_avg: float = float()
courses_avgs: list = list()
final_avg: float = float()

while True:
    input_data = input()
    if input_data == 'Finish':
        break
    course_name = input_data
    

print(f'{course_name} - {course_avg:.2f}.')
print(f'Student\'s final assessment is { sum(courses_avgs) / len(courses_avgs) :.2f}.')