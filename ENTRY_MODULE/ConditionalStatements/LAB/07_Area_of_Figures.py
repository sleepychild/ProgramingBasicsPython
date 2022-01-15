from math import pi


def square() -> float:
    side: float = float(input())
    return side * side


def rectangle() -> float:
    side_a: float = float(input())
    side_b: float = float(input())
    return side_a * side_b


def circle() -> float:
    return pi * float(input()) ** 2


def triangle() -> float:
    side: float = float(input())
    height: float = float(input())
    return (side * height) / 2


try:
    print(round(locals()[input()](), 3))
except KeyError as e:
    pass
