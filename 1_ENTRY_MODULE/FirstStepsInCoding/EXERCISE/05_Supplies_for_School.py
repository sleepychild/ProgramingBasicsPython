pen_pack_price = 5.8
marker_pack_price = 7.2
cleaner_ltr_price = 1.2

total = pen_pack_price * int(input())
total += marker_pack_price * int(input())
total += cleaner_ltr_price * int(input())


def discount(percent: int) -> float:
    return abs(int(percent) - 100) * 0.01


print(total * discount(int(input())))
