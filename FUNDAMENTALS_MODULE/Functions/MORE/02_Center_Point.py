from math import sqrt, floor
from typing import List


def distance_to_center(x: float, y: float) -> float:
    return sqrt( x**2 + y**2 )

point_a: List[float] = [float(input()), float(input())]
point_b: List[float] = [float(input()), float(input())]

if distance_to_center(*point_a) <= distance_to_center(*point_b):
    print(f'({floor(point_a[0])}, {floor(point_a[1])})')
else:
    print(f'({floor(point_b[0])}, {floor(point_b[1])})')
