arr: list = list()
for i in range(int(input())): arr.append(int(input()))
arr.sort()

arr_max: int = arr[-1]
arr_diff: int = int(abs(sum(arr[:-1])-arr_max))

print(f'Yes\nSum = {arr_max}' if arr_diff == 0 else f'No\nDiff = {arr_diff}')
