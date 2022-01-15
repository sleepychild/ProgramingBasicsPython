height: int = int(input())
data: str = str()

for i in range( 1, height + 1 ):
    data += '*' * i  + '\n'

for i in range( height - 1, 0, -1 ):
    data += '*' * i + '\n'

print(data, end='')
