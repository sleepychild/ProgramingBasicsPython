numbers = (num for num in range(1, int(input())+1))
nums: int = 1
run: bool = True

while run:
    line: str = str()
    for _ in range(nums):
        try:
            line += f'{next(numbers)} '
        except StopIteration as e:
            run = False
            continue
    print(line)
    nums += 1
