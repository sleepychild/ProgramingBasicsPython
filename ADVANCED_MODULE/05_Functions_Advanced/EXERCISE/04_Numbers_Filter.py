def even_odd_filter(**kwargs):
    return_data = {}
    for k, v in kwargs.items():
        return_data[k] = list(
            filter(
                {
                    "even": lambda x: (x % 2) == 0,
                    "odd": lambda x: (x % 2) == 1,
                }[k],
                v,
            )
        )
    return dict(sorted(return_data.items(), key=lambda x: len(x[1]), reverse=True))


print(
    even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    )
)

print(
    even_odd_filter(
        odd=[2, 2, 30, 44, 10, 5],
    )
)
