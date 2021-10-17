steps_target: int = 10000
steps_count: int = int()
going_home: bool = bool()

while True:
    input_data: str = input()
    going_home = input_data == 'Going home'

    if going_home:
        steps_count += int(input())
    else:
        steps_count += int(input_data)
    
    if steps_count >= steps_target:
        print(f'Goal reached! Good job!\n{steps_count - steps_target} steps over the goal!')
        exit(0)
    elif going_home:
        print(f'{steps_target - steps_count} more steps to reach goal.')
        exit(0)
