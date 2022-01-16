snowballs_score: list = list()

for _ in range(int(input())):
    snowballs_score.append([int(input()), int(input()), int(input())])

snowballs_score.sort(key=lambda x: (x[0]/x[1])**x[2], reverse=True)
best_snowball: list = snowballs_score[0]

print(f'{best_snowball[0]} : {best_snowball[1]} = {int((best_snowball[0]/best_snowball[1])**best_snowball[2])} ({best_snowball[2]})')
