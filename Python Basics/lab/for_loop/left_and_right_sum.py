number = int(input())

left_sum = 0
right_sum =0

for left in range(number):
    left_sum += int(input())

for right in range(number):
    right_sum += int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f'No, diff = {diff}')