numbers: list = []

while True:
    data_in = input()
    if data_in == 'Stop':
        break
    numbers.append(int(data_in))

numbers.sort()
print(numbers[-1])
