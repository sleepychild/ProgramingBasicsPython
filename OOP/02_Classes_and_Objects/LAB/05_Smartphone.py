from typing import List


class Smartphone:
    def __init__(
        self, memory: int, apps: List[str] = list(), is_on: bool = bool()
    ) -> None:
        self.memory: int = memory
        self.apps: List[str] = apps
        self.is_on: bool = is_on

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        if self.memory >= app_memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
