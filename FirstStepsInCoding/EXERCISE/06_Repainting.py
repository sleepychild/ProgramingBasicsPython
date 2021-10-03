nylon_price: float = 1.5
paint_price: float = 14.5
paint_thinner_price: float = 5
bags: float = .4

total: float = bags
total += nylon_price * (int(input()) + 2)
total += paint_price * (int(input()) * 1.1)
total += paint_thinner_price * int(input())
total += (total * .3) * int(input())

print(total)
