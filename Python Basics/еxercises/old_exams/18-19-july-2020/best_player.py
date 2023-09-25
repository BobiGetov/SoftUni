player_name = ''
best_achievement = 0

while True:
    input_name = input()

    if input_name == 'END':
        break

    scored_goals = int(input())

    if scored_goals > best_achievement:
        best_achievement = scored_goals
        player_name = input_name

    if scored_goals >= 10:
        break

print(f'{player_name} is the best player!')

if best_achievement >= 3:
    print(f'He has scored {best_achievement} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_achievement} goals.')
