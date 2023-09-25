total_days = 1
climbed_meters = 5364

while True:
    rest = input()

    if rest == 'END':
        break
    if rest == 'Yes':
        total_days += 1

    current_climbed_meters = int(input())
    climbed_meters += current_climbed_meters

    if climbed_meters >= 8848:
        break

    if total_days == 5:
        break
if climbed_meters >= 8848:
    print(f'Goal reached for {total_days} days!')

else:
    print('Failed!')
    print(f'{climbed_meters}')