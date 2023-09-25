budget = float(input())
needed_fuel = float(input())
day_of_week = input()

needed_money = (needed_fuel * 2.10) + 100

if day_of_week == 'Saturday':
    needed_money -= needed_money * 0.10

elif day_of_week == 'Sunday':
    needed_money -= needed_money * 0.20

diff = abs(needed_money - budget)

if budget >= needed_money:
    print(f'Safari time! Money left: {diff:.2f} lv.')

else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')