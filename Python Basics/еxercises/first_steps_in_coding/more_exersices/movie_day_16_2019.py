from math import ceil
time_for_shoot = int(input())
scenes_number = int(input())
scene_duration = int(input())

prep_on_ground = (time_for_shoot * 0.15)

total_time_needed = (scenes_number * scene_duration) + prep_on_ground

time_left = abs(total_time_needed - time_for_shoot)

if total_time_needed <= time_for_shoot:
    print(f"You managed to finish the movie on time! You have {time_left:.0f} minutes left!")
elif total_time_needed > time_for_shoot:
    print(f'Time is up! To complete the movie you need {time_left:.0f} minutes.')