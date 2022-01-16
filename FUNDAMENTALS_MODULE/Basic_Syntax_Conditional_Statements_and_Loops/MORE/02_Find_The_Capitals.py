input_str: str = input()
indices: list = list()
for i in range(len(input_str)):
    if input_str[i].isupper():
        indices.append(i)
print(indices)
