for number in range(int(input()), int(input())+1):
    digit_list: list = []
    for digit in str(number):
        digit_list.append(int(digit))
    if sum(digit_list[::2]) == sum(digit_list[1::2]): print(number, end=' ')
