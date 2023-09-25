budget = int(input())
season = input()
number_of_fishers = int(input())

price = 0

if season == 'Spring':
    price = 3000
    if number_of_fishers <= 6:
        price -= price * 0.10
    elif 7 <= number_of_fishers <= 11:
        price -= price * 0.15
    elif number_of_fishers >= 12:
        price -= price * 0.25
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if number_of_fishers <= 6:
        price -= price * 0.10
    elif 7 <= number_of_fishers <= 11:
        price -= price * 0.15
    elif number_of_fishers >= 12:
        price -= price * 0.25
elif season == 'Winter':
    price = 2600
    if number_of_fishers <= 6:
        price -= price * 0.10
    elif 7 <= number_of_fishers <= 11:
        price -= price * 0.15
    elif number_of_fishers >= 12:
        price -= price * 0.25

if number_of_fishers % 2 == 0 and season in 'Summer Winter Spring':
    price -= price * 0.05

diff = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
elif budget <= price:
    print(f'Not enough money! You need {diff:.2f} leva.')