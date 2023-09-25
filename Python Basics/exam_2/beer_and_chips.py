from math import ceil

fan_name = input()
budget = float(input())
beer_bottles_number = int(input())
chips_number = int(input())

beers_price = beer_bottles_number * 1.20
chips_price = beers_price * 0.45
total_chips_price = ceil(chips_price * chips_number)

total_price = total_chips_price + beers_price

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'{fan_name} bought a snack and has {diff:.2f} leva left.')

elif budget < total_price:
    print(f'{fan_name} needs {diff:.2f} more leva!')