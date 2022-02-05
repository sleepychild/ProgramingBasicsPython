data_type: str = input()
data_value: str = input()

if data_type == 'int':
    print(int(data_value)*2)
elif data_type == 'real':
    print(f'{float(data_value)*1.5:.2f}')
else:
    print(f'${data_value}$')
