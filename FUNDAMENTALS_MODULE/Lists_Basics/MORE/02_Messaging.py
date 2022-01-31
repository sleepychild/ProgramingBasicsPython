from typing import List

# cypher: str = '9992 562 8933'
# text_in: List[str] = list('This is some message for you')

# cypher: str = '2 122 1123 1321 9 17211'
# text_in: List[str] = list('87j973u59dg37e725!')

cypher: str = input()
text_in: List[str] = list(input())

text_out: str = str()

for i in [sum([int(y) for y in x]) for x in cypher.split(" ")]:
    text_len: int = len(text_in)
    text_out += text_in.pop(i if text_len >= i else i % text_len)

print(text_out)
