age: int = int(input())
cost: float = float(input())
toy: int = int(input())

total: float = float()

for i in range(1,age+1,2):
    total+= toy

cash: int = 10
for i in range(2,age+1,2):
    total+=cash-1
    cash+=10

diff: float = total - cost

print(f'Yes! {diff:.2f}' if diff >= 0 else f'No! {abs(diff):.2f}')
