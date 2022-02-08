from typing import List

num_list: List[int] = [ int(x) for x in input().split(', ')]

print('Positive:', ', '.join( [ str(x) for x in filter(lambda x: x >= 0, num_list) ] ))
print('Negative:', ', '.join( [ str(x) for x in filter(lambda x: x < 0, num_list) ] ))
print('Even:', ', '.join( [ str(x) for x in filter(lambda x: x % 2 == 0, num_list) ] ))
print('Odd:', ', '.join( [ str(x) for x in filter(lambda x: x % 2 != 0, num_list) ] ))
