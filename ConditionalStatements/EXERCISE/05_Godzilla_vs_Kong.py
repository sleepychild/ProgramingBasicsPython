budget: float = float(input()) * .9
extras: int = int(input())
extras_costume_price: float = float(input())

extras_costume_expense = (extras * extras_costume_price) * .9 if extras > 150 else extras * extras_costume_price
leftover = round(budget - extras_costume_expense, 2)

if leftover < 0:
    print('Not enough money!\nWingard needs {:.2f} leva more.'.format(abs(leftover)))
else:
    print('Action!\nWingard starts filming with {:.2f} leva left.'.format(leftover))
