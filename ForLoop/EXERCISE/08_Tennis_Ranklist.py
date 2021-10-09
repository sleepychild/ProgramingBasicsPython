from math import floor

tournaments_result_names: tuple = ('W', 'F', 'SF',)
tournaments_result_points: tuple = (2000, 1200, 720,)

tournaments_count: int = int(input())
points_initial: int = int(input())

points_won: int = int()
tournaments_results: list = list()

for _ in range(tournaments_count):
    tournaments_results.append(input())

for tournament_result in tournaments_results:
    points_won+= tournaments_result_points[tournaments_result_names.index(tournament_result)]

print(f'Final points: {points_won+points_initial}')
print(f'Average points: {floor(points_won/tournaments_count)}')
print(f'{tournaments_results.count("W")/tournaments_count*100:.2f}%')
