while True:
    destination = input()

    if destination == 'End':
        break
    min_budget = float(input())
    saved_money = 0

    while saved_money < min_budget:
        savings = float(input())
        saved_money += savings
    print(f'Going to {destination}!')
