number_of_pairs = int(input())

number_1, number_2 = 0, 0
condition = True
pair_sum = number_1 + number_2
value = 0
maxdiff = 0

for i in range(number_of_pairs):
    number_1 = int(input())
    number_2 = int(input())

    for _ in range(number_of_pairs):
        current_sum = number_1 + number_2

    if pair_sum == current_sum:
        value = current_sum
    else:
        diff = abs(pair_sum - current_sum)
        if diff > maxdiff:
            maxdiff = diff

if condition:
    print(f'Yes, value={value}')
else:
    print(f'No, maxdiff={maxdiff}')
