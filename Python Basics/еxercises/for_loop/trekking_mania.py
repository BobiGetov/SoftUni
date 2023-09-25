number_of_groups = int(input())

total_climbers = 0

musala, monblan, kili, k2, everest = 0, 0, 0, 0, 0

for _ in range(number_of_groups):
    group_number = int(input())
    total_climbers += group_number

    if group_number <= 5:
        musala += group_number
    elif 6<= group_number <=12:
        monblan += group_number
    elif 13<= group_number <= 25:
        kili += group_number
    elif 26<= group_number <= 40:
        k2 += group_number
    elif 41<= group_number:
        everest += group_number

print(f'{musala / total_climbers * 100:.2f}%')
print(f'{monblan / total_climbers * 100:.2f}%')
print(f'{kili / total_climbers * 100:.2f}%')
print(f'{k2 / total_climbers * 100:.2f}%')
print(f'{everest / total_climbers * 100:.2f}%')