actor_name: str = input()
total: float = float(input())
judges_count: int = int(input())

for _ in range(judges_count):
    total+= (len(input())*float(input()))/2
    if total >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total:.1f}!')
        exit(0)

print(f'Sorry, {actor_name} you need {(1250.5-total):.1f} more!')
