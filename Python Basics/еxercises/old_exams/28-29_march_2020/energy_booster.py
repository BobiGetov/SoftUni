fruit = input()
set = input()
purchased_sets = int(input())

price = 0

if fruit == 'Watermelon':
    if set == 'small':
        price = 56 * 2
    elif set == 'big':
        price = 28.70 * 5

elif fruit == 'Mango':
    if set == 'small':
        price = 36.66 * 2
    elif set == 'big':
        price = 19.60 * 5

elif fruit == 'Pineapple':
    if set == 'small':
        price = 42.10 * 2
    elif set == 'big':
        price = 24.80 * 5

elif fruit == 'Raspberry':
    if set == 'small':
        price = 20 * 2
    elif set == 'big':
        price = 15.20 * 5

total_price = purchased_sets * price

if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15
elif 1000 < total_price:
    total_price -= total_price * 0.50

print(f'{total_price:.2f} lv.')