from typing import List

words_in: List[List[str]] = [ list(w) for w in input().split(" ")]
words_out: List[str] = list()

for word_in in words_in:
    word_out: str = str()
    nums: List[str] = list()
    ltrs: List[str] = list()
    for l in word_in:
        if l.isnumeric():
            nums.append(l)
        else:
            ltrs.append(l)
    word_out += chr(int(''.join(nums)))
    try:
        word_out += ltrs.pop(-1)
        ltrs.append(ltrs.pop(0))
    except IndexError:
        pass
    word_out += ''.join(ltrs)
    words_out.append(word_out)

print(' '.join(words_out))
