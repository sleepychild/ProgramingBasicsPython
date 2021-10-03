budget: float = float(input())

vga_qty: int = int(input())
cpu_qty: int = int(input())
ram_qty: int = int(input())

vga_price: float = 250.00 * .85 if vga_qty > cpu_qty else 250.00
vga_cost: float = vga_price * vga_qty

cpu_price: float = vga_cost * .35
cpu_cost: float = cpu_price * cpu_qty

ram_price: float = vga_cost * .1
ram_cost: float = ram_price * ram_qty

total_cost = vga_cost + cpu_cost + ram_cost

if budget >= total_cost:
    print('You have {:.2f} leva left!'.format(budget - total_cost))
else:
    print('Not enough money! You need {:.2f} leva more!'.format(abs(budget - total_cost)))
