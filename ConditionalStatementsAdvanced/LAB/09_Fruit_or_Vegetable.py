fruit: list = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable: list = ['tomato', 'cucumber', 'pepper', 'carrot']

thing = input()

if thing in fruit:
    print('fruit')
elif thing in vegetable:
    print('vegetable')
else:
    print('unknown')
