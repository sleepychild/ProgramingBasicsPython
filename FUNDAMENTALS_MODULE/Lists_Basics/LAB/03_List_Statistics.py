from typing import List

input_val: int = int()
pos_list: List = list()
neg_list: List = list()

for _ in range(int(input())):
    input_val = int(input())
    (neg_list if input_val < 0 else pos_list).append(input_val)

print(pos_list)
print(neg_list)
print(f"Count of positives: {len(pos_list)}")
print(f"Sum of negatives: {sum(neg_list)}")
