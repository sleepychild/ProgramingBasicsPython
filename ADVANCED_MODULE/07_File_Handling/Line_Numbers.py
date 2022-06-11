from re import compile

reg_ex_letters = compile(r"[A-Za-z]")

reg_ex_punctuation = compile(
    r"[\!\"\#\$\%\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\\\]\^\_\`\{\|\}\~]"
)

with open("text.txt", "rt") as file_in:
    with open("output.txt", "wt") as file_out:
        file_out.writelines(
            [
                f"Line {k}: {v.strip()} ({len(reg_ex_letters.findall(v))})({len(reg_ex_punctuation.findall(v))})\n"
                for k, v in enumerate(file_in.readlines(), 1)
            ]
        )
