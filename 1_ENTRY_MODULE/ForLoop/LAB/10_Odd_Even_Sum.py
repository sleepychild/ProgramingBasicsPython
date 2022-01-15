arr: list = list()
for i in range(int(input())): arr.append(int(input()))

even_sum: int = sum(arr[1::2])
odd_sum: int = sum(arr[::2])

print(f'Yes\nSum = {even_sum}' if even_sum == odd_sum else f'No\nDiff = {abs(even_sum - odd_sum)}')
