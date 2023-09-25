age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_per_birthday = 0
odd_birthday = 0
even_birthday = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_per_birthday += 10
        odd_birthday += money_per_birthday - 1
    else:
        even_birthday += 1

total_toys_price = even_birthday * toy_price
savings = total_toys_price + odd_birthday
diff = abs(savings - washing_machine_price)

if savings >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
elif savings < washing_machine_price:
    print(f'No! {diff:.2f}')