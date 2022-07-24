from .task import Task
from typing import List


class Section:
    def __init__(self, name: str, tasks: List[Task] = list()) -> None:
        self.name: str = name
        self.tasks: List[Task] = tasks.copy()

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
