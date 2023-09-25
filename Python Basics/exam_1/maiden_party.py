maiden_party_price = float(input())
love_letters_number = int(input())
wax_roses_number = int(input())
key_holder_number = int(input())
cartoon_numbers = int(input())
luck_surprise_number = int(input())

purchased_items = love_letters_number + wax_roses_number + cartoon_numbers + luck_surprise_number

love_letters_price = love_letters_number * 0.60
wax_roses_price = wax_roses_number * 7.20
key_holder_price = key_holder_number * 3.60
cartoon_price = cartoon_numbers * 18.20
luck_surprise_price = luck_surprise_number * 22

total_price = love_letters_price + wax_roses_price + key_holder_price + cartoon_price + luck_surprise_price

if purchased_items >= 25:
    total_price -= total_price * 0.35

total_price -= total_price * 0.10
diff = abs(total_price - maiden_party_price)

if total_price >= maiden_party_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')