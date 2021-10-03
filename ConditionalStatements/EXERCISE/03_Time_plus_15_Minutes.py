from datetime import datetime, time, date, timedelta
time_start: time = time(hour=int(input()), minute=int(input()))
time_diff: timedelta = timedelta(minutes=15)
time_fmt: str = "%-H:%M"
print((datetime.combine(date.today(), time_start) + time_diff).strftime(time_fmt))
