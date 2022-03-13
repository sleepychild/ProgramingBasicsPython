from typing import List


class Class:
    __students_count: int = 22

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.students: List[str] = list()
        self.grades: List[float] = list()

    def add_student(self, name: str, grade: float) -> None:
        if len(self.students) < self.__class__.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self) -> float:
        return round(sum(self.grades) / len(self.grades), 2)

    def __repr__(self) -> str:
        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {self.get_average_grade()}'


# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)
