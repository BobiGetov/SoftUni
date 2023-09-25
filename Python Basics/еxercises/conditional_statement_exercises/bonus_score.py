points = int(input())
bonus = 0

if points <= 100:
    bonus += 5
elif 100 < points <=1000:
    bonus += points * 0.20
elif points > 1000:
    bonus += points * 0.10

sum_points = points + bonus
extra_points = 0

if points % 2 == 0:
    extra_points += + 1
elif points % 10 == 5:
    extra_points += + 2

final_bonus = bonus + extra_points
total_points = sum_points + extra_points

print(final_bonus)
print(total_points)