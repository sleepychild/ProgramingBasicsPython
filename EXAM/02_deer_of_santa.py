from math import floor, ceil

days_absent: int = int(input())
food_left: int = int(input())

deer_one_consumption: float = float(input())
deer_two_consumption: float = float(input())
deer_three_consumption: float = float(input())

deer_one_needed: float = deer_one_consumption * days_absent
deer_two_needed: float = deer_two_consumption * days_absent
deer_three_needed: float = deer_three_consumption * days_absent

needed_total: float = deer_one_needed + deer_two_needed + deer_three_needed

food_diff: float = food_left - needed_total

if food_diff >= 0:
    print(f'{floor(food_diff)} kilos of food left.')
else:
    print(f'{ceil(abs(food_diff))} more kilos of food are needed.')
