type_of_fuel = input()
tank_fuel_lt = float(input())

if type_of_fuel == 'Diesel' or type_of_fuel == 'Gasoline' or type_of_fuel == 'Gas':
    if tank_fuel_lt >= 25:
        print(f'You have enough {type_of_fuel.lower()}.')
    elif tank_fuel_lt < 25:
        print(f'Fill your tank with {type_of_fuel.lower()}!')
else:
    print('Invalid fuel!')
