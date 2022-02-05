from typing import List

def is_palindrome(num_str: str) -> bool:
    num_str_len: int = len(num_str)
    num_str_mid: int = num_str_len // 2
    if num_str_len == 1:
        return True
    elif (num_str_len % 2) == 0:
        return num_str[:num_str_mid] == num_str[num_str_mid:][::-1]
    else:
        return num_str[:num_str_mid] == num_str[num_str_mid+1:][::-1]

input_data: List[str] = input().split(', ')

for i in input_data:
    print(is_palindrome(i))
