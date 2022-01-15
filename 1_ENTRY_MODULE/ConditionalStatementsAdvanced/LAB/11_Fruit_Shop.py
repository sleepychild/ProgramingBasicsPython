weekdays: list = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

fruit: list = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']

work_day: list = [2.50, 1.2,  .85, 1.45, 2.7, 5.5, 3.85]
week_end: list = [2.7,  1.25, .9,  1.6,  3,   5.6, 4.2 ]

try:
    f = fruit.index(input())
    if weekdays.index(input()) <= 4:
        print('{:.2f}'.format(work_day[f] * float(input())))
    else:
        print('{:.2f}'.format(week_end[f] * float(input())))
except:
    print('error')
