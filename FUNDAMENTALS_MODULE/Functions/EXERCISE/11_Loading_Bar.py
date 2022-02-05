data_in: str = input()

if data_in == '100':
    print('100% Complete!\n[%%%%%%%%%%]')
else:
    data_progress: int = int(data_in[0])
    print(f'{data_in}% [{"".join([ "%" if x <= data_progress else "." for x in range(1, 11) ])}]\nStill loading...')
