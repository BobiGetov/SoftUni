minutes_walk_per_day = int(input())
number_daily_walks = int(input())
calories = int(input())

daily_walks_minutes = minutes_walk_per_day * number_daily_walks

calories_burned = daily_walks_minutes * 5
calories_need_to_burn = calories * 0.5

if calories_burned >= calories_need_to_burn:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
elif calories_burned < calories_need_to_burn:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')