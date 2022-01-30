from typing import Set

terminated: bool = False
card_set: Set = set(input().split(" "))
team_a_player_count: int = 11
team_b_player_count: int = 11

for card in card_set:
    if card.startswith('A'):
        team_a_player_count -= 1
    else:
        team_b_player_count -= 1
    if team_a_player_count < 7 or team_b_player_count < 7:
        terminated = True
        break

print(f'Team A - {team_a_player_count}; Team B - {team_b_player_count}')
if terminated:
    print('Game was terminated')
