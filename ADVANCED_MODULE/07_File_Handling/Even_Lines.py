def print_modified(str_in: str) -> None:
    for x in (
        "-",
        ",",
        ".",
        "!",
        "?",
    ):
        str_in = str_in.replace(x, "@")
    print(str_in)


with open("text.txt", "rt") as f:
    [
        print_modified(" ".join(reversed(line.strip().split())))
        for line in f.readlines()[::2]
    ]
