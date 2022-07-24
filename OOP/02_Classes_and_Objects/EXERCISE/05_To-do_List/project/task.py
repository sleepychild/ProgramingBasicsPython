from typing import List


class Task:
    def __init__(
        self,
        name: str,
        due_date: str,
        comments: List = list(),
        completed: bool = bool(),
    ) -> None:
        self.name: str = name
        self.due_date: str = due_date
        self.comments: List = comments.copy()
        self.completed: bool = completed

    def change_name(self, new_name: str) -> str:
        if self.name == new_name:
            return "Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date: str) -> str:
        if self.due_date == new_date:
            return "Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        try:
            self.comments[comment_number] = new_comment
        except IndexError as _:
            return "Cannot find comment."
        else:
            return ", ".join(self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
