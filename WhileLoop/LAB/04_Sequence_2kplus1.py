def num_seq(target: int, start: int = 1):
    current: int = start
    while target >= current:
        yield current
        current = current * 2 + 1

if __name__ == '__main__':
    for i in num_seq(int(input())):
        print(i)
