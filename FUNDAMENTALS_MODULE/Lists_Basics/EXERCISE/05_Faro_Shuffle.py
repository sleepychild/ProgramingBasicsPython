from typing import List

def shuffle(deck_in: List[str]) -> List[str]:
    deck_out: List[str] = deck_in
    deck_len: int = len(deck_in)//2
    deck_a: List[str] = deck_in[:deck_len]
    deck_b: List[str] = deck_in[deck_len:]
    deck_out[::2] = deck_a
    deck_out[1::2] = deck_b
    return deck_out

cards: List[str] = input().split(' ')

for _ in range(int(input())):
    cards = shuffle(cards)

print(cards)
