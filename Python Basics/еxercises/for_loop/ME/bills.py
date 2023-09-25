months = int(input())

electricity = 0
water = 20 * months
internet = 15 * months
other = 0

for _ in range(months):
    current_electricity = float(input())
    electricity += current_electricity
    other += (current_electricity + 15 + 20) * 1.2

total_sum = electricity + water + internet + other

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {total_sum / months:.2f} lv')