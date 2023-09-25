from math import floor

series_name = input()
seasons_number = int(input())
episodes_number = int(input())
episode_duration = float(input())

adverts = episode_duration * 0.2
total_episode_duration = episode_duration + adverts
total_episodes = seasons_number * episodes_number
special_episodes = seasons_number * 10

total_watching_time = (total_episodes * total_episode_duration) + special_episodes

formatted = floor(total_watching_time)

print(f'Total time needed to watch the {series_name} series is {formatted} minutes.')
