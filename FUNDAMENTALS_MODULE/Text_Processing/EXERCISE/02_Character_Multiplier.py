str_a, str_b = input().split()
len_a, len_b = len(str_a), len(str_b)
sum_op: int = int()

if len_a > len_b:
    for c in str_a[len_b:]:
        sum_op += ord(c)
elif len_b > len_a:
    for c in str_b[len_a:]:
        sum_op += ord(c)

for a, b in zip(str_a, str_b):
    sum_op += ord(a) * ord(b)

print(sum_op)