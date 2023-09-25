from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
rest_time = break_duration * 1 / 4
remaining_time = (break_duration - lunch_time - rest_time)

diff =ceil(abs(remaining_time - episode_duration))

if remaining_time >= episode_duration:
    print(f'You have enough time to watch {series_name} and left with {diff} minutes free time.')
elif remaining_time < episode_duration:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")
