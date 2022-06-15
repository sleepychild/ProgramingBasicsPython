def rectangle(length: int, width: int) -> str:
    if not all([isinstance(length, int), isinstance(width, int)]):
        return "Enter valid values!"
    area = lambda: length * width
    perimeter = lambda: (length + width) * 2
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle("2", 10))
