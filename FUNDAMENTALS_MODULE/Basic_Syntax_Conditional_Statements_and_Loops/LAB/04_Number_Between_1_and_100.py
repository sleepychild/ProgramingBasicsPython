while True:
    input_number: float = float(input())
    if 1 <= input_number <= 100:
        print(f'The number {input_number} is between 1 and 100')
        exit(0)
