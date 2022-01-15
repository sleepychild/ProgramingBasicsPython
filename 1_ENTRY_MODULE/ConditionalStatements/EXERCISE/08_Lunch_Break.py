from math import ceil

series_name: str = input()
episode_runtime: int = int(input())
lunch_break_duration: int = int(input())

timer: int = lunch_break_duration
timer -= episode_runtime
timer -= lunch_break_duration / 8
timer -= lunch_break_duration / 4

if timer >= 0:
    print(f'You have enough time to watch {series_name} and left with {ceil(timer)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {ceil(abs(timer))} more minutes.')
