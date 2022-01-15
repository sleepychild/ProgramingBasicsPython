the_book: str = input()
try_count: int = int()
search: str = str()

while True:
    search = input()
    if search == 'No More Books':
        print(f'The book you search is not here!\nYou checked {try_count} books.')
        exit(0)
    elif the_book == search:
        print(f'You checked {try_count} books and found it.')
        exit(0)
    else:
        try_count += 1
