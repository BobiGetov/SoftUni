from math import floor

numbers_of_tournaments = int(input())
start_points = int(input())

winner = 2000
finalist = 1200
semi_finalist = 720

total_tournament_points = 0
number_of_wins = 0

for _ in range(numbers_of_tournaments):
    stage_reached = input()

    if stage_reached == 'W':
        total_tournament_points += winner
        number_of_wins += 1

    elif stage_reached == 'F':
        total_tournament_points += finalist

    elif stage_reached == 'SF':
        total_tournament_points += semi_finalist

rank_list_points = total_tournament_points + start_points


print(f'Final points: {rank_list_points}')
print(f'Average points: {floor(total_tournament_points / numbers_of_tournaments)}')
print(f'{number_of_wins / numbers_of_tournaments * 100:.2f}%')