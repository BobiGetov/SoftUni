strawberries_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberries_kg = float(input())

raspberry_price = strawberries_price / 2
orange_price = raspberry_price - (raspberry_price * 0.40)
bananas_price = raspberry_price - (raspberry_price * 0.80)

total_raspberry = raspberry_kg * raspberry_price
total_orange = orange_kg * orange_price
total_bananas = bananas_kg * bananas_price
total_strawberries = strawberries_kg * strawberries_price

needed_money = total_bananas + total_raspberry + total_orange + total_strawberries

print(f'{needed_money:.2f}')
