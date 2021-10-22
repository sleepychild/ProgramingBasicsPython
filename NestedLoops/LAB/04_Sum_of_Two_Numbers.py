a: int = int(input())
b: int = int(input())
m: int = int(input())

if m/2 < a or m/2 > b:
    print(f'{((b-a)+1)**2} combinations - neither equals {m}')
elif m <= b:
    print(f'Combination N:{m-1} (1 + {m-1} = {m})')
else:
    a_at: int = m - b
    combination: int = ( ( a_at - a ) + 1 ) * ( ( b - a ) + 1 )
    print(f'Combination N:{combination} ({a_at} + {b} = {m})')
