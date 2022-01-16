key: int = int(input())
length: int = int(input())
msg: str = str()

for _ in range(length):
    msg += chr(ord(input())+key)

print(msg)
