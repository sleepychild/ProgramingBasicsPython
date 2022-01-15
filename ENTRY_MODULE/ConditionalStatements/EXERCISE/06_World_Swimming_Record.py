record_in_sec: float = float(input())
distance_in_m: float = float(input())
sec_per_m: float = float(input())

time_in_sec = (distance_in_m * sec_per_m) + (distance_in_m // 15) * 12.5

if record_in_sec > time_in_sec:
    print('Yes, he succeeded! The new world record is {:.2f} seconds.'.format(time_in_sec))
else:
    print('No, he failed! He was {:.2f} seconds slower.'.format(time_in_sec - record_in_sec))
