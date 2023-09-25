contract_term = input()
contract_type = input()
mobile_internet = input()
months_to_pay = int(input())

price = 0

if contract_term == 'one':
    if contract_type == 'Small':
        price = 9.98

    elif contract_type == 'Middle':
        price = 18.99

    elif contract_type == 'Large':
        price = 25.98

    elif contract_type == 'ExtraLarge':
        price = 35.99

elif contract_term == 'two':
    if contract_type == 'Small':
        price = 8.58

    elif contract_type == 'Middle':
        price = 17.09

    elif contract_type == 'Large':
        price = 23.59

    elif contract_type == 'ExtraLarge':
        price = 31.79

if mobile_internet == 'yes':
    if price <= 10:
        price += 5.50

    elif 10 < price <= 30:
        price += 4.35

    elif 30 < price:
        price += 3.85

total_price = months_to_pay * price

if contract_term == 'two':
    total_price -= total_price * 0.0375

print(f'{total_price:.2f} lv.')