dog_food_price = 2.50
cat_food_price = 4

dog_food_pack = int(input())
cat_food_pack = int(input())

dog_food_sum = dog_food_price * dog_food_pack
cat_food_sum = cat_food_price * cat_food_pack

total_sum = dog_food_sum + cat_food_sum

print(f'{total_sum} lv.')