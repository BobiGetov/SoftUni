flower_type = input()
flower_number = int(input())
budget = int(input())

flower_price = 0

if flower_type == 'Roses':
    flower_price = 5
    if flower_number > 80:
        flower_price -= flower_price * 0.10
elif flower_type == 'Dahlias':
    flower_price = 3.80
    if flower_number > 90:
        flower_price -= flower_price * 0.15
elif flower_type == 'Tulips':
    flower_price = 2.80
    if flower_number > 80:
        flower_price -= flower_price * 0.15
elif flower_type == 'Narcissus':
    flower_price = 3
    if flower_number < 120:
        flower_price += flower_price * 0.15
elif flower_type == 'Gladiolus':
    flower_price = 2.50
    if flower_price < 80:
        flower_price += flower_price * 0.20

total_sum = flower_price * flower_number
diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f'Hey, you have a great garden with {flower_number} {flower_type} and {diff:.2f} leva left.')
elif total_sum > budget:
    print(f'Not enough money, you need {diff:.2f} leva more.')