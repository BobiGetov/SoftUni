from math import ceil

average_speed = float(input())
lit_per_100_km = float(input())

total_distance = 384400 * 2
time_to_go_and_back = ceil(total_distance / average_speed)
total_time = time_to_go_and_back + 3
fuel = (lit_per_100_km*total_distance)/100

print(total_time)
print(f'{fuel:.0f}')

