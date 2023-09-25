month = input()
hours_spent = int(input())
group_number = int(input())
day_time = input()

price_per_hour = 0

if month == 'march' or month == 'april' or month == 'may':
    if day_time == 'day':
        price_per_hour = 10.50

    elif day_time == 'night':
        price_per_hour = 8.40

elif month == 'june' or month == 'july' or month == 'august':
    if day_time == 'day':
        price_per_hour = 12.60

    elif day_time == 'night':
        price_per_hour = 10.20

if group_number >= 4:
    price_per_hour -= price_per_hour * 0.10

if hours_spent >= 5:
    price_per_hour -= price_per_hour * 0.50

total_price = hours_spent * price_per_hour * group_number

print(f'Price per person for one hour: {price_per_hour:.2f}')
print(f'Total cost of the visit: {total_price:.2f}')
