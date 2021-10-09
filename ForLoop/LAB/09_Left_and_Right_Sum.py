arr: list = list()
for i in range(int(input())*2): arr.append(int(input()))

left_sum: int = sum(arr[:int(len(arr)/2)])
right_sum: int = sum(arr[int(len(arr)/2):])

print(f'Yes, sum = {left_sum}' if left_sum == right_sum else f'No, diff = {abs(left_sum - right_sum)}')
