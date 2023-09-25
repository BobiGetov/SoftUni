tournament_days = int(input())

total_raised_money = 0
win_days = 0
loose_days = 0

for day in range(tournament_days):
    daily_raised_money = 0
    daily_wins = 0
    daily_lose = 0

    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()

        if result == 'win':
            daily_raised_money += 20
            daily_wins += 1

        elif result == 'lose':
            daily_lose += 1

    if daily_wins > daily_lose:
        daily_raised_money += daily_raised_money * 0.10

    total_raised_money += daily_raised_money
    win_days += daily_wins
    loose_days += daily_lose

if win_days > loose_days:
    total_raised_money += total_raised_money * 0.20
    print(f'You won the tournament! Total raised money: {total_raised_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_raised_money:.2f}')