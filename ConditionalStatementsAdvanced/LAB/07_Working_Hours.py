weekdays: list = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

hour: int = int(input())

if weekdays.index(input()) <= 5 and (hour >= 10 and hour <= 18):
    print('open')
else:
    print('closed')
