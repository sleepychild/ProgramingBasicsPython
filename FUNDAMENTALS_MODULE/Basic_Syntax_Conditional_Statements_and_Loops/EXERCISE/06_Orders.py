orders_count: int = int(input())
total_price: float = float()

for _ in range(orders_count):
    capsule_price: float = float(input())
    days: int = int(input())
    capsule_count: int = int(input())
    price: float = (capsule_count * days) * capsule_price
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')
