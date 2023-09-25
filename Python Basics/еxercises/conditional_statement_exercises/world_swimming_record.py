from math import floor

record_in_seconds = float(input())
distance_in_m = float(input())
time_for_m_in_seconds = float(input())

water_resistance = floor(distance_in_m / 15)
water_resistance_slowdown = water_resistance * 12.5
time_score = (distance_in_m * time_for_m_in_seconds) + water_resistance_slowdown
record_diff = abs(record_in_seconds - time_score)

if time_score < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {time_score:.2f} seconds.')
elif time_score >= record_in_seconds:
    print(f'No, he failed! He was {record_diff:.2f} seconds slower.')
