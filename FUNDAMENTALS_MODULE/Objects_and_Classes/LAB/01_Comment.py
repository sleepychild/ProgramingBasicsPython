import string


class Comment:
    def __init__(self, username:  str, content: str, likes: int = 0) -> None:
        self.username: str = username
        self.content: str = content
        self.likes: int = likes
