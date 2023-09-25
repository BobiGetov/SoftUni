needed_money = float(input())
money_on_hand = float(input())
total_day_counter = 0
spend_day_counter = 0

while True:
    action = input()

    if action == 'spend':
        spended_money = float(input())
        money_on_hand -= spended_money
        spend_day_counter += 1
        total_day_counter += 1

        if money_on_hand < 0:
            money_on_hand = 0

        if spend_day_counter == 5:
            print("You can't save the money.")
            print(f'{total_day_counter}')
            break
    elif action == 'save':
        saved_money = float(input())
        money_on_hand += saved_money
        spend_day_counter = 0
        total_day_counter += 1
        if money_on_hand >= needed_money:
            print(f'You saved the money for {total_day_counter} days.')
            break
