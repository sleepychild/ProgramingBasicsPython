score_str: str = input()
score_int: int = int(score_str)
bonus: int = 2 if score_str.endswith("5") else 1 if (score_int % 2) == 0 else 0
bonus += 5 if score_int <= 100 else score_int * .2 if score_int < 1000 else score_int * .1
print(f'{bonus}\n{bonus + score_int}')
