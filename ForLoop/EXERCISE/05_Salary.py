websites: tuple = ('Facebook', 'Instagram', 'Reddit',)
fines: tuple = (150, 100, 50,)

tabs_count: int = int(input())
salary: int = int(input())

for _ in range(tabs_count):
    try:
        salary-= fines[websites.index(input())]
    except:
        pass
    if salary <= 0:
        print('You have lost your salary.')
        exit(0)

print(salary)
