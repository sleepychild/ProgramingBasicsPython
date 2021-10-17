vacation_expence: float = float(input())
balance: float = float(input())
days: int = int()
days_spending: int = int()

def spend(ammount: float) -> None:
    global days_spending, balance
    days_spending += 1
    balance = max(0, balance - ammount)

def save(ammount: float) -> None:
    global days_spending, balance
    days_spending = 0
    balance = balance + ammount

while True:
    days += 1
    locals()[input()](float(input()))

    if days_spending >= 5:
        print(f'You can\'t save the money.\n{days}')
        exit(0)

    if balance >= vacation_expence:
        print(f'You saved the money for {days} days.')
        exit(0)
