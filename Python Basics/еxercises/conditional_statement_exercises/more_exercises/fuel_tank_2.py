type_of_fuel = input()
fuel_amount = float(input())
club_card = input()

fuel_price = 0

if type_of_fuel == 'Gasoline':
    fuel_price = 2.22
    if club_card == 'Yes':
        fuel_price = fuel_price - 0.18

elif type_of_fuel == 'Diesel':
    fuel_price = 2.33
    if club_card == 'Yes':
        fuel_price = fuel_price - 0.12
elif type_of_fuel == 'Gas':
    fuel_price = 0.93
    if club_card == 'Yes':
        fuel_price = fuel_price - 0.08

total_price = fuel_price * fuel_amount

if 20 <= fuel_amount <= 25:
    total_price -= total_price * 0.08
elif 25 < fuel_amount:
    total_price -= total_price * 0.10

print(f'{total_price:.2f} lv.')