from typing import List

result_elements: List[str] = list()
for i in range(ord(input())+1,ord(input())):
    result_elements.append(chr(i))

print(' '.join(result_elements))
