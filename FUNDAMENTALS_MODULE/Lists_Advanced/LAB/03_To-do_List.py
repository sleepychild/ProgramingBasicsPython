from typing import List


class TaskItem:
    def __init__(self, importance: int = 0, description: str = '') -> None:
        self.importance: int = importance
        self.description: str = description

    def __lt__(self, other: 'TaskItem'):
        return self.importance < other.importance

    def __gt__(self, other: 'TaskItem'):
        return self.importance > other.importance

    def __le__(self, other: 'TaskItem'):
        return self.importance <= other.importance

    def __ge__(self, other: 'TaskItem'):
        return self.importance >= other.importance

    def __eq__(self, other: 'TaskItem'):
        return self.importance == other.importance and self.description == other.description

    def __ne__(self, other: 'TaskItem'):
        return self.importance != other.importance and self.description != other.description

    def __str__(self) -> str:
        return self.description

class TaskList:
    def __init__(self) -> None:
        self.tasks: List[TaskItem] = list()
    
    def add_task(self, importance: int = 0, description: str = '') -> None:
        self.tasks.append(TaskItem(importance, description))
        self.tasks.sort()
    
    def __str__(self) -> str:
        descriptions: List[str] = [ str(t) for t in self.tasks ]
        return str(descriptions)

task_list: TaskList = TaskList()
data_in: str = str()

while True:
    data_in = input()

    if data_in == 'End':
        print(task_list)
        exit(0)

    importance, description = data_in.split('-')
    task_list.add_task(int(importance), description)
