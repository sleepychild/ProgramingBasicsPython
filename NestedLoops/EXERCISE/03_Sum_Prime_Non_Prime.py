p_sum: int = int()
n_sum: int = int()

def is_prime(num: int, last_digit: str) -> bool:
    prime_nums_list: list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if num in prime_nums_list:
        return True
    elif last_digit in ['2', '5']:
        return False
    else:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True

input_data: str = str()
input_num: int = int()
while True:
    input_data = input()
    if input_data == 'stop':
        break
    input_num = int(input_data)
    if input_num < 0:
        print('Number is negative.')
    elif is_prime(int(input_data), input_data[-1]):
        p_sum += input_num
    else:
        n_sum += input_num

print(f'Sum of all prime numbers is: {p_sum}\nSum of all non prime numbers is: {n_sum}')
