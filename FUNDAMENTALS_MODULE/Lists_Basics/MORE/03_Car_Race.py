from typing import List, Tuple

# data_in: List[int] = [ int(x) for x in '29 13 9 0 13 0 21 0 14 82 12'.split() ]
# data_in: List[int] = [ int(x) for x in '123 20 4 0 13 0 0 5 5 14 0'.split() ]
data_in: List[int] = [ int(x) for x in input().split() ]

data_split: int = len(data_in)//2

def race_cars_evaluation(car_times: List) -> float:
    car_time_total: float = float()
    for car_time in car_times:
        if car_time == 0:
            car_time_total *= .8
        else:
            car_time_total += car_time
    return car_time_total

def race(left_car_data: List[int], right_car_data: List[int]) -> Tuple[str, float]:
    left_car_time: float = race_cars_evaluation(left_car_data)
    right_car_time: float = race_cars_evaluation(right_car_data)
    # print(left_car_time, right_car_time)
    return ('left', left_car_time,) if left_car_time < right_car_time else ('right', right_car_time,)

winner, winner_time = race(data_in[:data_split], data_in[data_split:][:0:-1])
# print(data_in[:data_split], data_in[data_split:][:0:-1])

print(f'The winner is {winner} with total time: {winner_time:.1f}')
