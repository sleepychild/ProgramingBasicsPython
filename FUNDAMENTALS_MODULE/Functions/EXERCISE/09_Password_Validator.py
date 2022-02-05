password_str: str = input()

has_ltr: bool = bool()
has_dgt: int = int()
has_spc: bool = bool()

has_len: bool = 6 <= len(password_str) <= 10

for s in password_str:
    if s.isalpha():
        has_ltr = True
    elif s.isnumeric():
        has_dgt += 1
    elif not s.isalnum():
        has_spc = True

if not has_spc and has_ltr and has_len and has_dgt >= 2:
    print('Password is valid')
    exit(0)
elif not has_len:
    print('Password must be between 6 and 10 characters')

if has_spc:
    print('Password must consist only of letters and digits')

if has_dgt < 2:
    print('Password must have at least 2 digits')
