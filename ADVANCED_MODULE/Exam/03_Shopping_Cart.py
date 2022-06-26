def shopping_cart(*args) -> str:
    group_limits = {
        "Dessert": 2,
        "Pizza": 4,
        "Soup": 3,
    }

    data_dict = {
        "Dessert": list(),
        "Pizza": list(),
        "Soup": list(),
    }

    for arg in args:
        if arg == "Stop":
            break

        group, product = arg

        if (
            len(data_dict[group]) < group_limits[group]
            and not product in data_dict[group]
        ):
            data_dict[group].append(product)

    for group in data_dict.keys():
        data_dict[group].sort()

    data_dict = dict(sorted(data_dict.items(), key=lambda x: len(x[1]), reverse=True))

    data_str: str = str()

    for k, v in data_dict.items():
        data_str += f"{k}:\n"
        for e in v:
            data_str += f" - {e}\n"

    if any(data_dict.values()):
        return data_str
    else:
        return "No products in the cart!"


print(
    shopping_cart(
        ("Pizza", "ham"),
        ("Soup", "carrots"),
        ("Pizza", "cheese"),
        ("Pizza", "flour"),
        ("Dessert", "milk"),
        ("Pizza", "mushrooms"),
        ("Pizza", "tomatoes"),
        "Stop",
    )
)

print(
    shopping_cart(
        ("Pizza", "ham"),
        ("Dessert", "milk"),
        ("Pizza", "ham"),
        "Stop",
    )
)

print(
    shopping_cart(
        "Stop",
        ("Pizza", "ham"),
        ("Pizza", "mushrooms"),
    )
)
