data_input: str = input()
data_input = data_input.split(' ')
for i in range(len(data_input)):
    data_input[i] = int(data_input[i]) * -1
print(data_input)
