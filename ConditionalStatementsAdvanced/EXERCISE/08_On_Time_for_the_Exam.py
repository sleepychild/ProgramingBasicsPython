from datetime import datetime, time, date, timedelta

start_time: datetime = datetime.combine(date.today(), time(hour=int(input()), minute=int(input())))
arived: datetime = datetime.combine(date.today(), time(hour=int(input()), minute=int(input())))

def time_diff(a, st, b_or_a) -> None:
    h, m = divmod(abs((a - st).total_seconds()/60), 60)
    # time_diff: str = datetime.combine(date.today(), time(hour=int(h), minute=int(m))).strftime("%-M" if h == 0 else "%-H:%M")
    td: str = f'{m:.0f}' if h == 0 else datetime.combine(date.today(), time(hour=int(h), minute=int(m))).strftime("%-H:%M")
    tds: str = "minutes" if h == 0 else "hours"
    print(f'{td} {tds} {b_or_a} the start')

if start_time == arived:
    print('On time')
    exit(0)

arive_time: datetime = start_time - timedelta(minutes=30)

if start_time >= arived >= arive_time:
    print('On time')
    time_diff(arived, start_time, 'before')
elif arive_time > arived:
    print('Early')
    time_diff(arived, start_time, 'before')
else:
    print('Late')
    time_diff(arived, start_time, 'after')
