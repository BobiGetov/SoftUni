from math import floor, ceil
days_number = int(input())
food_lefover_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_gr = float(input())

dog_food_needed = days_number * dog_food_per_day_kg
cat_food_needed = days_number * cat_food_per_day_kg
turtle_food_needed = (days_number * turtle_food_per_day_gr) / 1000

total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed

diff = abs(total_food_needed - food_lefover_kg)

if total_food_needed <= food_lefover_kg:
    print(f'{floor(diff)} kilos of food left.')
elif total_food_needed > food_lefover_kg:
    print(f'{ceil(diff)} more kilos of food are needed.')
