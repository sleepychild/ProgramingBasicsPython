weekdays: list = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

try:
    print("Working day" if weekdays.index(input()) <= 4 else "Weekend")
except ValueError as e:
    print("Error")
