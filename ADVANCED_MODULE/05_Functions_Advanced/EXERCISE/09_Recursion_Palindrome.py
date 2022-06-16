def palindrome(word, index):
    if index == 0:
        return f"{word} is{' ' if all([word[index] == word[-1 - index],palindrome(word, index+1),]) else ' not '}a palindrome"
    elif index <= len(word) // 2:
        return all(
            [
                word[index] == word[-1 - index],
                palindrome(word, index + 1),
            ]
        )
    else:
        return word[index] == word[-1 - index]


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
