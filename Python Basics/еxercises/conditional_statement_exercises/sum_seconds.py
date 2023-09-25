first, second, third = int(input()), int(input()), int(input())
time_sum = first + second + third
seconds = time_sum % 60
minutes = time_sum // 60

print(f'{minutes}:{seconds:02d}')