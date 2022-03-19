from typing import List
lin: List[str] = input().split(', ')
print(dict(zip(lin, [ ord(c) for c in lin ])))
