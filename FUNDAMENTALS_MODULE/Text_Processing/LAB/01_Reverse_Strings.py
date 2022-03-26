while True:
    lin: str = input()
    if lin == 'end': break
    print(f"{lin} = {''.join(reversed(lin))}")
    # print(f"{lin} = {lin[::-1]}")
