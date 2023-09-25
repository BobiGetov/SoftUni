from math import  floor , ceil
sqm_vines = int(input())
grape_per_sqm = float(input())
needed_liters_wine = int(input())
number_of_workers = int(input())

set_aside = sqm_vines * 0.40
grape = grape_per_sqm * set_aside
liters_wine = grape / 2.5

leftover = abs(liters_wine - needed_liters_wine)
wine_per_worker = leftover / number_of_workers

if liters_wine < needed_liters_wine:
    print(f'It will be a tough winter! More {floor(leftover)} liters wine needed.')

elif liters_wine >= needed_liters_wine:
    print(f'Good harvest this year! Total wine: {floor(liters_wine)} liters.')
    print(f'{ceil(leftover)} liters left -> {ceil(wine_per_worker)} liters per person.')