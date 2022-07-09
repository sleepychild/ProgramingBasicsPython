class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name: str = name
        self.language: str = language
        self.skills: int = skills

    def watch_course(self, course_name: str, language: str, skill_earned: int) -> str:
        if self.language == language:
            self.skills += skill_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills <= skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"
        elif self.language == new_language:
            return f"{self.name} already knows {self.language}"
        else:
            res: str = f"{self.name} switched from {self.language} to {new_language}"
            self.language = new_language
            return res
