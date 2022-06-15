# abcdefghijklmnopqrstuvwxyz


def sorting_cheeses(**kwargs) -> str:
    cheeses = sorted(kwargs.items())
    cheeses.sort(key=lambda x: len(x[1]), reverse=True)
    output_data = list()
    for cheese, pieces in cheeses:
        output_data.append(cheese)
        for piece in sorted(pieces, reverse=True):
            output_data.append(str(piece))
    return "\n".join(output_data)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
