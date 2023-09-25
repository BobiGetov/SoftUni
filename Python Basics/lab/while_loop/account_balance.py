total = 0

while True:
    current_sum = input()

    if current_sum == 'NoMoreMoney':
        break

    current_sum = float(current_sum)

    if current_sum < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {current_sum:.2f}')
    total += current_sum

print(f'Total: {total:.2f}')