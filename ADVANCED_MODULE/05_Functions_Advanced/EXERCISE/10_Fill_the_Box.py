def fill_the_box(*args):
    h, l, w, *other = args
    free_space = (h * l * w) - sum(other[: other.index("Finish")])
    return (
        f"There is free space in the box. You could put {free_space} more cubes."
        if free_space > 0
        else f"No more free space! You have {abs(free_space)} more cubes."
    )


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
