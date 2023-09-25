joinery_number = int(input())
joinery_dimensions = input()
delivery = input() # 60 lv
joinery_price = 0
total_price = 0
flag = True

if joinery_number < 10:
    flag = False
    print('Invalid order')

elif joinery_dimensions == '90X130':
    joinery_price = 110
    if 30 <= joinery_number < 60:
        joinery_price -= joinery_price * 0.05
    elif joinery_number > 60:
        joinery_price -= joinery_price * 0.08

elif joinery_dimensions == '100X150':
    joinery_price = 140
    if 40 <= joinery_number < 80:
        joinery_price -= joinery_price * 0.06
    elif joinery_number > 80:
        joinery_price -= joinery_price * 0.10

elif joinery_dimensions == '130X180':
    joinery_price = 190
    if 20 <= joinery_number < 50:
        joinery_price -= joinery_price * 0.07
    elif joinery_number > 50:
        joinery_price -= joinery_price * 0.12

elif joinery_dimensions == '200X300':
    joinery_price = 250
    if 25 <= joinery_number < 50:
        joinery_price -= joinery_price * 0.09
    elif joinery_number > 50:
        joinery_price -= joinery_price * 0.14

total_price = joinery_number * joinery_price

if delivery == 'With delivery':
    total_price += 60

if joinery_number > 99:
    total_price -= total_price * 0.04

if flag:
    print(f'{total_price:.2f} BGN')