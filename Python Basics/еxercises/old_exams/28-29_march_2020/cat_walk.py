day_walk = int(input())
walk_number_daily = int(input())
calories = int(input())

burned_calories = day_walk * walk_number_daily * 5

if calories / 2 <= burned_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')