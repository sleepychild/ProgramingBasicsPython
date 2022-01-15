days: int = int(input())
qty: float = float()
deg: float = float()

ltrs: float = float()
dgrs: float = float()

for day in range(days):
    ltrs = float(input())
    dgrs = float(input())

    qty += ltrs
    deg += ltrs * dgrs

deg_avg: float = deg/qty

print(f'Liter: {qty:.2f}')
print(f'Degrees: {deg_avg:.2f}')
print('Not good, you should baking!' if deg_avg < 38 else 'Super!' if deg_avg <= 42 else 'Dilution with distilled water!')
