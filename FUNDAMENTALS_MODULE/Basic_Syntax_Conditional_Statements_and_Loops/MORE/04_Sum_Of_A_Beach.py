words: tuple = ('sand', 'water', 'fish', 'sun',)
input_str: str = input().lower()
counter: int = int()
for word in words:
    counter += input_str.count(word)
print(counter)
