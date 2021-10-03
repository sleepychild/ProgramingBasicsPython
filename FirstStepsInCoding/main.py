# LAB

# 01. Hello SoftUni
# print("Hello SoftUni")

# 02. Nums 1...10
# for i in range(1, 11, 1):
#     print(i)

# 03. Rectangle Area
# print(int(input()) * int(input()))

# 04. Inches to Centimeters
# print(2.54 * float(input()))

# 05. Greeting by Name
# print(f'Hello, {input()}!')

# 06. Concatenate Data
# print(f'You are {input()} {input()}, a {input()}-years old person from {input()}.')

# 07. Projects Creation
# name = input()
# projects = int(input())
# time = projects * 3
# print( f'The architect {name} will need {time} hours to complete {projects} project/s.' )

# 08. Pet Shop
# dog_food = int(input()) * 2.5
# cat_food = int(input()) * 4
# total = dog_food + cat_food
# print(f'{total} lv.')

# 09. Yard Greening
# price = float(input()) * 7.61
# discount = price * 0.18
# final = price - discount
# print(f'The final price is: {final} lv.\nThe discount is: {discount} lv.')

# EXERCISE

# 01. USD to BGN
# print(1.79549 * float(input()))

# 02. Radians to Degrees
# from math import floor, pi
# print(float(input()) * 180 / pi)

# 03. Deposit Calculator
# deposit = float(input())
# period = int(input())
# rate = float(input()) * 0.01
# print(deposit + period * ((deposit * rate) / 12))

# 04. Vacation books list
# pages = int(input())
# pph = int(input())
# days = int(input())
# print(int((pages / pph)/days))
# # OR
# print(int((int(input()) / int(input()))/int(input())))

# 05. Supplies for School
# def discount(percent: int) -> float:
#     return abs(int(percent) - 100) * 0.01


# pen_pack_price = 5.8
# marker_pack_price = 7.2
# cleaner_ltr_price = 1.2

# total = pen_pack_price * int(input())
# total += marker_pack_price * int(input())
# total += cleaner_ltr_price * int(input())
# print(total * discount(int(input())))

# 06. Repainting
# nylon_price: float = 1.5
# paint_price: float = 14.5
# paint_thinner_price: float = 5
# bags: float = .4

# total: float = bags
# total += nylon_price * (int(input()) + 2)
# total += paint_price * (int(input()) * 1.1)
# total += paint_thinner_price * int(input())
# total += (total * .3) * int(input())

# print(total)

# 07. Food Delivery
# bird_menu: float = 10.35
# fish_menu: float = 12.4
# fucking_looser_menu: float = 8.15
# desert: float = 1.2
# delivery: float = 2.5

# total: float = float()
# total += bird_menu * int(input())
# total += fish_menu * int(input())
# total += fucking_looser_menu * int(input())

# print(total * desert + delivery)

# 08. Basketball Equipment
# training: int = int(input())

# shoes: float = training * .6
# kit: float = shoes * .8
# ball: float = kit / 4
# acc: float = ball / 5

# print(training + shoes + kit + ball + acc)

# 09. Fish Tank
print(((int(input()) * int(input()) * int(input())) / 1000) * (1 - (float(input()) * 0.01)))
