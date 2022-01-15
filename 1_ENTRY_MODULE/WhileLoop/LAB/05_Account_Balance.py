data_in: str = str()
balance: float = float()
deposit: float = float()

while True:
    data_in = input()
    
    if data_in == 'NoMoreMoney':
        break
    
    deposit = float(data_in)
    
    if deposit < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {deposit:.2f}')
    balance += deposit

print(f'Total: {balance:.2f}')
