length = float(input())
width = float(input())

width_in_cm = width * 100
length_in_cm = length * 100
corridor = width_in_cm - 100

desks_in_width = corridor // 70
desks_in_length = length_in_cm // 120

total_desks = (desks_in_width * desks_in_length) - 3

print(format(total_desks,".2f"))