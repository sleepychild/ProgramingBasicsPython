# LAB

# 01. Excellent Result
# print("Excellent!" if float(input()) >= 5.5 else "")

# 02. Greater Number
# a: int = int(input())
# b: int = int(input())
# print(a if a >= b else b)

# 03. Even or Odd
# print("even" if (int(input()) % 2) == 0 else "odd")

# 04. Password Guess
# print("Welcome" if input() == 's3cr3t!P@ssw0rd' else "Wrong password!")

# 05. Number 100...200
# a: int = int(input())
# print("Less than 100" if a < 100 else "Greater than 200" if a > 200 else "Between 100 and 200")

# 06. Speed Info
# a: float = float(input())
# print(
#     "slow" if a <= 10 else
#     "average" if a <= 50 else
#     "fast" if a <= 150 else
#     "ultra fast" if a <= 1000 else
#     "extremely fast"
# )

# 07. Area of Figures
# from math import pi


# def square() -> float:
#     side: float = float(input())
#     return side * side


# def rectangle() -> float:
#     side_a: float = float(input())
#     side_b: float = float(input())
#     return side_a * side_b


# def circle() -> float:
#     return pi * float(input()) ** 2


# def triangle() -> float:
#     side: float = float(input())
#     height: float = float(input())
#     return (side * height) / 2


# try:
#     print(round(locals()[input()](), 3))
# except KeyError as e:
#     pass

# EXERCISE

# 01. Sum Seconds
# from datetime import time
# minutes, seconds = divmod(int(input()) + int(input()) + int(input()), 60)
# print(time(minute=minutes, second=seconds).strftime("%-M:%S"))

# 02. Bonus Score
# score_str: str = input()
# score_int: int = int(score_str)
# bonus: int = 2 if score_str.endswith("5") else 1 if (score_int % 2) == 0 else 0
# bonus += 5 if score_int <= 100 else score_int * .2 if score_int < 1000 else score_int * .1
# print(f'{bonus}\n{bonus + score_int}')

# 03. Time + 15 Minutes
# from datetime import datetime, time, date, timedelta
# time_start: time = time(hour=int(input()), minute=int(input()))
# time_diff: timedelta = timedelta(minutes=15)
# time_fmt: str = "%-H:%M"
# print((datetime.combine(date.today(), time_start) + time_diff).strftime(time_fmt))

# 04. Toy Shop
# price_list: dict = {
#     "jigsaw": 2.6,
#     "talking_doll": 3,
#     "plush_bear": 4.1,
#     "minion": 8.2,
#     "truck": 2,
# }

# vacation_expenses: float = float(input())

# order_items: dict = {
#     "jigsaw": int(input()),
#     "talking_doll": int(input()),
#     "plush_bear": int(input()),
#     "minion": int(input()),
#     "truck": int(input()),
# }

# order_items_count: int = int()
# order_value: float = float()

# for k, v in order_items.items():
#     order_items_count += v
#     order_value += v * price_list[k]

# profit = (order_value * .75) * .9 if order_items_count >= 50 else order_value * .9
# leftover = round(profit - vacation_expenses, 2)

# print(
#     'Yes! {:.2f} lv left.'.format(leftover) if leftover >= 0 else
#     'Not enough money! {:.2f} lv needed.'.format(abs(leftover))
# )

# 05. Godzilla vs. Kong
# budget: float = float(input()) * .9
# extras: int = int(input())
# extras_costume_price: float = float(input())

# extras_costume_expense = (extras * extras_costume_price) * .9 if extras > 150 else extras * extras_costume_price
# leftover = round(budget - extras_costume_expense, 2)

# if leftover < 0:
#     print('Not enough money!\nWingard needs {:.2f} leva more.'.format(abs(leftover)))
# else:
#     print('Action!\nWingard starts filming with {:.2f} leva left.'.format(leftover))

# 06. World Swimming Record
# record_in_sec: float = float(input())
# distance_in_m: float = float(input())
# sec_per_m: float = float(input())

# time_in_sec = (distance_in_m * sec_per_m) + (distance_in_m // 15) * 12.5

# if record_in_sec > time_in_sec:
#     print('Yes, he succeeded! The new world record is {:.2f} seconds.'.format(time_in_sec))
# else:
#     print('No, he failed! He was {:.2f} seconds slower.'.format(time_in_sec - record_in_sec))

# 07. Shopping
# budget: float = float(input())

# vga_qty: int = int(input())
# cpu_qty: int = int(input())
# ram_qty: int = int(input())

# vga_price: float = 250.00 * .85 if vga_qty > cpu_qty else 250.00
# vga_cost: float = vga_price * vga_qty

# cpu_price: float = vga_cost * .35
# cpu_cost: float = cpu_price * cpu_qty

# ram_price: float = vga_cost * .1
# ram_cost: float = ram_price * ram_qty

# total_cost = vga_cost + cpu_cost + ram_cost

# if budget >= total_cost:
#     print('You have {:.2f} leva left!'.format(budget - total_cost))
# else:
#     print('Not enough money! You need {:.2f} leva more!'.format(abs(budget - total_cost)))

# 08. Lunch Break
from math import ceil

# series_name: str = input()
# episode_runtime: int = int(input())
# lunch_break_duration: int = int(input())

# timer: int = lunch_break_duration
# timer -= episode_runtime
# timer -= lunch_break_duration / 8
# timer -= lunch_break_duration / 4

# if timer >= 0:
#     print(f'You have enough time to watch {series_name} and left with {ceil(timer)} minutes free time.')
# else:
#     print(f'You don\'t have enough time to watch {series_name}, you need {ceil(abs(timer))} more minutes.')
