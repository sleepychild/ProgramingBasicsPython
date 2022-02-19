from typing import List, Tuple

TAX_RATE: float = .2
DISCOUNT: float = .9

INVALID_PRICE: str = 'Invalid price!'
INVALID_ORDER: str = 'Invalid order!'

SPC: str = 'special'
RGL: str = 'regular'

total: float = float()

while True:
    in_data: str = input()
    if in_data in [SPC, RGL]:
        customer = in_data
        break
    else:
        charge: float = float(in_data)
        if charge > 0:
            total += charge
        else:
            print(INVALID_PRICE)

taxes: float = total * TAX_RATE

if customer == SPC:
    final: float = (total + taxes) * DISCOUNT
else:
    final: float = total + taxes

receipt: str = f'''Congratulations you've just bought a new computer!
Price without taxes: {total:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {final:.2f}$
'''

if final > 0:
    print(receipt)
else:
    print(INVALID_ORDER)
