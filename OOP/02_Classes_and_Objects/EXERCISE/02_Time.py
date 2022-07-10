from typing import ClassVar


class Time:
    max_hours: ClassVar[int] = 23
    max_minutes: ClassVar[int] = 59
    max_seconds: ClassVar[int] = 59

    def __init__(
        self, hours: int = int(), minutes: int = int(), seconds: int = int()
    ) -> None:
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def set_time(
        self, hours: int = int(), minutes: int = int(), seconds: int = int()
    ) -> None:
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self) -> str:
        self.seconds += 1
        if self.seconds > type(self).max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > type(self).max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > type(self).max_hours:
                    self.hours = 0
        return self.get_time()
