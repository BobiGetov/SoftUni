game_moves = int(input())

i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0
invalid_numbers = 0
total_sum = 0

for i in range(game_moves):
    current_number = int(input())

    if current_number < 0 or current_number > 50:
        invalid_numbers += 1
        total_sum = total_sum / 2

    elif 0 <= current_number <= 50:
        if 0 <= current_number <= 9:
            i1 += 1
            total_sum += current_number * 0.2

        elif 10 <= current_number <= 19:
            i2 += 1
            total_sum += current_number * 0.3

        elif 20 <= current_number <= 29:
            i3 += 1
            total_sum += current_number * 0.4

        elif 30 <= current_number <= 39:
            i4 += 1
            total_sum += 50

        elif 40 <= current_number <= 50:
            i5 += 1
            total_sum += 100

print(f'{total_sum:.2f}')
print(f'From 0 to 9: {i1 / game_moves * 100:.2f}%')
print(f'From 10 to 19: {i2 / game_moves * 100:.2f}%')
print(f'From 20 to 29: {i3 / game_moves * 100:.2f}%')
print(f'From 30 to 39: {i4 / game_moves * 100:.2f}%')
print(f'From 40 to 50: {i5 / game_moves * 100:.2f}%')
print(f'Invalid numbers: {invalid_numbers / game_moves * 100:.2f}%')
