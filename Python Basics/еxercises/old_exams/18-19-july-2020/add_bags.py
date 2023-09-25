price_over_kg = float(input())
luggage_kg = float(input())
days_to_trip = int(input())
luggage_number = int(input())

current_price = 0

if luggage_kg < 10:
    current_price = price_over_kg * 0.20
elif 10 <= luggage_kg <= 20:
    current_price = price_over_kg * 0.50
elif luggage_kg > 20:
    current_price = price_over_kg

if days_to_trip > 30:
    current_price += current_price * 0.10
elif 7 <= days_to_trip <= 30:
    current_price += current_price * 0.15
elif days_to_trip < 7:
    current_price += current_price * 0.40

total_price = luggage_number * current_price
print(f'The total price of bags is: {total_price:.2f} lv.')