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
    print(weekdays[int(input())-1])
except IndexError as e:
    print("Error")
