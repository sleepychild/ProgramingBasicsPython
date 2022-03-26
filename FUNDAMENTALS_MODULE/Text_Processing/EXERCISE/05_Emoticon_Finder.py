lin: str = input()
emot_index: int = -1

while True:
    emot_index: int = lin.find(':', emot_index+1)
    if emot_index == -1 or emot_index+1 == len(lin):
        break
    if not lin[emot_index+1].isspace():
        print(lin[emot_index:emot_index+2])
