number_of_cargo = int(input())

total_tons = 0

minibus_tons, minibus_price = 0, 0
truck_tons, truck_price = 0, 0
train_tons, train_price = 0, 0

for _ in range(number_of_cargo):
    current_cargo_tons = int(input())
    total_tons += current_cargo_tons

    if current_cargo_tons <= 3:
        minibus_tons += current_cargo_tons
        minibus_price += current_cargo_tons * 200

    elif 4 <= current_cargo_tons <= 11:
        truck_tons += current_cargo_tons
        truck_price += current_cargo_tons * 175

    elif 12 <= current_cargo_tons:
        train_tons += current_cargo_tons
        train_price += current_cargo_tons * 120

total_sum_prices = minibus_price + truck_price + train_price

print(f'{total_sum_prices / total_tons:.2f}')
print(f'{minibus_tons / total_tons * 100:.2f}%')
print(f'{truck_tons / total_tons * 100:.2f}%')
print(f'{train_tons / total_tons * 100:.2f}%')
