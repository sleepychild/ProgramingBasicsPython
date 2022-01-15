rates: dict = {
    'Sofia':   [.050, .070, .080, .120],
    'Varna':   [.045, .075, .100, .130],
    'Plovdiv': [.055, .080, .120, .145],
}

city: str = input()
sales: float = float(input())

if (not city in rates.keys()) or sales < 0:
    print('error')
    exit(0)

rate: int = (
    0 if sales <= 500 else
    1 if sales <= 1000 else
    2 if sales <= 10000 else
    3
)

print('{:.2f}'.format(rates[city][rate] * sales))
