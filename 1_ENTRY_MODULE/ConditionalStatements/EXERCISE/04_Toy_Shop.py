price_list: dict = {
    "jigsaw": 2.6,
    "talking_doll": 3,
    "plush_bear": 4.1,
    "minion": 8.2,
    "truck": 2,
}

vacation_expenses: float = float(input())

order_items: dict = {
    "jigsaw": int(input()),
    "talking_doll": int(input()),
    "plush_bear": int(input()),
    "minion": int(input()),
    "truck": int(input()),
}

order_items_count: int = int()
order_value: float = float()

for k, v in order_items.items():
    order_items_count += v
    order_value += v * price_list[k]

profit = (order_value * .75) * .9 if order_items_count >= 50 else order_value * .9
leftover = round(profit - vacation_expenses, 2)

print(
    'Yes! {:.2f} lv left.'.format(leftover) if leftover >= 0 else
    'Not enough money! {:.2f} lv needed.'.format(abs(leftover))
)
