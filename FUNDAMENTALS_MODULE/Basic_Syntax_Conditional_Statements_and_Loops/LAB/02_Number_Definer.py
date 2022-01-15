input_number: float = float(input())

if input_number == 0:
    print('zero')
    exit(0)

input_number_sign: str = 'positive' if input_number > 0 else 'negative'

input_number_abs: float = abs(input_number)

if input_number_abs < 1:
    print(f'small {input_number_sign}')
elif input_number_abs > 1000000:
    print(f'large {input_number_sign}')
else:
    print(input_number_sign)
