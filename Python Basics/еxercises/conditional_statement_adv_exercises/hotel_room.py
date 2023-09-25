month = input()
number_of_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights < 14:
        studio_price -= studio_price * 0.05
    elif number_of_nights > 14:
        studio_price -= studio_price * 0.30

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price -= studio_price * 0.20

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if number_of_nights > 14:
    apartment_price -= apartment_price * 0.10

studio_total_sum = studio_price * number_of_nights
apartment_total_sum = apartment_price * number_of_nights

print(f'Apartment: {apartment_total_sum:.2f} lv.')
print(f'Studio: {studio_total_sum:.2f} lv.')