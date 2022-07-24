from typing import Union


class Account:
    def __init__(self, id: int, name: str, balance: int = int()) -> None:
        self.id: int = id
        self.name: str = name
        self.balance: int = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[int, str]:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"
