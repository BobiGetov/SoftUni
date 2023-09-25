import sys

n = int(input())

numbers_sum = 0
max_number = -sys.maxsize

for i in range(n):
    current_number = int(input())
    numbers_sum += current_number
    if current_number > max_number:
        max_number = current_number

total_sum = numbers_sum - max_number

if total_sum == max_number:
    print('Yes')
    print(f'Sum = {total_sum}')
else:
    diff = abs(total_sum - max_number)
    print('No')
    print(f'Diff = {diff}')
