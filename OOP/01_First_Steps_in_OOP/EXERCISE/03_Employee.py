class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int) -> None:
        self.id: int = id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: int = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        return self.salary * 12

    def raise_salary(self, amount: int) -> int:
        self.salary += amount
        return self.salary
