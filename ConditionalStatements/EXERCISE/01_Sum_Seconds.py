from datetime import time
minutes, seconds = divmod(int(input()) + int(input()) + int(input()), 60)
print(time(minute=minutes, second=seconds).strftime("%-M:%S"))
