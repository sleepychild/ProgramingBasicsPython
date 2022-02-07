from math import sqrt, floor


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x: float = x
        self.y: float = y

    def distance_to(self, p: 'Point') -> float:
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self) -> str:
        return f'({floor(self.x)}, {floor(self.y)})'


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start: Point = start
        self.end: Point = end
        self.length = self.start.distance_to(self.end)

    def __lt__(self, other: 'Line'):
        return self.length < other.length

    def __gt__(self, other: 'Line'):
        return self.length > other.length

    def __le__(self, other: 'Line'):
        return self.length <= other.length

    def __ge__(self, other: 'Line'):
        return self.length >= other.length

    def __eq__(self, other: 'Line'):
        return self.length == other.length

    def __ne__(self, other: 'Line'):
        return self.length != other.length

    def __str__(self) -> None:
        return str(self.start)+str(self.end)

    @classmethod
    def outward_line(cls, point_from: Point = Point(), point_a: Point = Point(), point_b: Point = Point()) -> 'Line':
        point_a_distance: float = point_a.distance_to(point_from)
        point_b_distance: float = point_b.distance_to(point_from)
        return cls(
            start=point_a if point_a_distance <= point_b_distance else point_b,
            end=point_b if point_a_distance <= point_b_distance else point_a
        )


CENTER: Point = Point()

line_a: Line = Line.outward_line(
    CENTER,
    Point(float(input()), float(input())),
    Point(float(input()), float(input()))
)

line_b: Line = Line.outward_line(
    CENTER,
    Point(float(input()), float(input())),
    Point(float(input()), float(input()))
)

print(
    line_a if line_a >= line_b else line_b
)
