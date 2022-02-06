from typing import List

def is_palindrome(s: str) -> bool:
    s_len: int = len(s)
    s_mid: int = s_len // 2
    if s_len == 1:
        return True
    elif (s_len % 2) == 0:
        return s[:s_mid] == s[s_mid:][::-1]
    else:
        return s[:s_mid] == s[s_mid+1:][::-1]

input_words: List[str] = list(filter(is_palindrome, input().split(' ')))
input_palin: str = input()

print(input_words)
print(f'Found palindrome {input_words.count(input_palin)} times')
