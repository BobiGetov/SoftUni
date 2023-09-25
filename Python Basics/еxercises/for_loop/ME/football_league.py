stadium_capacity = int(input())
number_of_all_fans = int(input())

a, b, v, g = 0, 0, 0, 0

for _ in range(number_of_all_fans):
    current_sector = input()

    if current_sector == 'A':
        a += 1
    elif current_sector == 'B':
        b += 1
    elif current_sector == 'V':
        v += 1
    elif current_sector == 'G':
        g += 1

print(f'{a / number_of_all_fans * 100:.2f}%')
print(f'{b / number_of_all_fans * 100:.2f}%')
print(f'{v / number_of_all_fans * 100:.2f}%')
print(f'{g / number_of_all_fans * 100:.2f}%')
print(f'{number_of_all_fans / stadium_capacity * 100:.2f}%')