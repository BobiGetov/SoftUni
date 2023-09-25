guest_number = int(input())
cover_price = float(input())
budget = float(input())

if 10 <= guest_number <= 15:
    cover_price -= cover_price * 0.15

elif 15 < guest_number <= 20:
    cover_price -= cover_price * 0.20

elif 20 < guest_number:
    cover_price -= cover_price * 0.25

birthday_cake_price = budget * 0.10

total_price = birthday_cake_price + (cover_price * guest_number)

diff = abs(budget - total_price)

if total_price <= budget:
    print(f'It is party time! {diff:.2f} leva left.')

elif total_price > budget:
    print(f'No party! {diff:.2f} leva needed.')