days_number = int(input())

total_liters_rakia = 0
total_alcohol_degree = 0

for i in range(days_number):
    liters_rakia = float(input())
    alcohol_degree = float(input())

    total_liters_rakia += liters_rakia
    total_alcohol_degree += alcohol_degree * liters_rakia

alcohol_degree = total_alcohol_degree / total_liters_rakia

print(f'Liter: {total_liters_rakia:.2f}')
print(f'Degrees: {alcohol_degree:.2f}')

if alcohol_degree < 38:
    print('Not good, you should baking!')
elif 38 <= alcohol_degree <= 42:
    print('Super!')
elif 42 < alcohol_degree:
    print('Dilution with distilled water!')
