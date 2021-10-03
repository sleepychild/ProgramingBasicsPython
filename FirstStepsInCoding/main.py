#!../venv/bin/python

# 02. Radians to Degrees
from math import floor, pi
print(float(input()) * 180 / pi)

# 03. Deposit Calculator
deposit = float(input())
period = int(input())
rate = float(input()) * 0.01
print(deposit + period * ((deposit * rate) / 12))

# 04. Vacation books list
pages = int(input())
pph = int(input())
days = int(input())
print(int((pages / pph)/days))
# OR
print(int((int(input()) / int(input()))/int(input())))

# 05. Supplies for School
def discount(percent: int) -> float:
    return abs(int(percent) - 100) * 0.01


pen_pack_price = 5.8
marker_pack_price = 7.2
cleaner_ltr_price = 1.2

total = pen_pack_price * int(input())
total += marker_pack_price * int(input())
total += cleaner_ltr_price * int(input())
print(total * discount(int(input())))

# 06. Repainting
print("Repainting")
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

# 07. Food Delivery
print("Food Delivery")
bird_menu: float = 10.35
fish_menu: float = 12.4
fucking_looser_menu: float = 8.15
desert: float = 1.2
delivery: float = 2.5

total: float = float()
total += bird_menu * int(input())
total += fish_menu * int(input())
total += fucking_looser_menu * int(input())

print(total * desert + delivery)

# 08. Basketball Equipment
print("Basketball Equipment")
training: int = int(input())

shoes: float = training * .6
kit: float = shoes * .8
ball: float = kit / 4
acc: float = ball / 5

print(training + shoes + kit + ball + acc)

# 09. Fish Tank
print("Fish Tank")
print(((int(input()) * int(input()) * int(input())) / 1000) * (1 - (float(input()) * 0.01)))
