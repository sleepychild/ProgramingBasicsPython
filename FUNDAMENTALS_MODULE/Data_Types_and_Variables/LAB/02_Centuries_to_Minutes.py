DAYS_IN_YEAR_AVERAGE: float = 365.2422

centuries: int = int(input())
years: int = centuries * 100
days: int = int(years * DAYS_IN_YEAR_AVERAGE)
hours: int = days * 24
minutes: int = hours * 60

print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
