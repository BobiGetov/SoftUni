house_height = float(input())
side_length = float(input())
roof_height = float(input())

front_door_area = 1.2 * 2
side_area = (house_height * house_height) * 2
total_front_and_back_side_area = side_area - front_door_area

windows_area = 1.5 * 1.5
left_and_right_area = side_length * house_height
total_left_and_right_area = (left_and_right_area * 2) - (windows_area * 2)

roof_area = ((house_height * roof_height) / 2) * 2

total_house_area = total_left_and_right_area + total_front_and_back_side_area
total_roof_area = roof_area + (left_and_right_area * 2)
# liter green paint - 3,4 sqm
# liter red paint - 4,3 sqm
green_paint = total_house_area / 3.4
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')