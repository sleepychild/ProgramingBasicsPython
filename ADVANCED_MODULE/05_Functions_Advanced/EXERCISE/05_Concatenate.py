def concatenate(*args, **kwargs):
    line_in = "".join(args)
    for k, v in kwargs.items():
        while k in line_in:
            line_in = line_in.replace(k, v)
    return line_in


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java="Java"))
