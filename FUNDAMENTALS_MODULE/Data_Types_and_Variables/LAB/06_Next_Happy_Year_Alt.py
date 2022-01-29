def check(yr: int) -> bool:
    y_str: str = str(yr)
    y_set: set = set(y_str)
    return len(y_str) == len(y_set)

year: int = int(input()) + 1

while not check(year):
    year += 1

print(year)
