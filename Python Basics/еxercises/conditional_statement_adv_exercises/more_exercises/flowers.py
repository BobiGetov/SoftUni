chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = chrysanthemums * 2
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50

elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15

total_flowers_number = chrysanthemums + roses + tulips
total_flowers_price = chrysanthemums_price + roses_price + tulips_price

if is_holiday == 'Y':
    total_flowers_price += total_flowers_price * 0.15

if tulips > 7 and season == 'Spring':
    total_flowers_price -= total_flowers_price * 0.05

elif roses >= 10 and season == 'Winter':
    total_flowers_price -= total_flowers_price * 0.10

if total_flowers_number > 20:
    total_flowers_price -= total_flowers_price * 0.20

bouquet = total_flowers_price + 2

print(f'{bouquet:.2f}')
