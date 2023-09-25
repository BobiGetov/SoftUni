from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

slowdown = floor((distance_in_meters // 50) * 30)

new_record = (distance_in_meters * seconds_per_meter) + slowdown

if new_record < record_in_seconds:
    print(f'Yes! The new record is {new_record:.2f} seconds.')
else:
    diff = abs(record_in_seconds - new_record)
    print(f'No! He was {diff:.2f} seconds slower.')
