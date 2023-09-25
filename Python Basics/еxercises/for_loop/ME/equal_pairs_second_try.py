numbers = int(input())

num_1 = 0
num_2 = 0
n = 1
pair_sum = 0
value = 0
maxdiff = 0
con = True

for i in range(2 * numbers):

    if i % 2 == 0:
        num_1 = int(input())
    else:
        num_2 = int(input())

    if n == i:
        n += 2
        current_sum = num_1 + num_2
        if pair_sum != 0:
            if current_sum == pair_sum:
                value = current_sum
                con = True
            else:
                diff = abs(current_sum - pair_sum)
                con = False
                if maxdiff <= diff:
                    maxdiff = diff
            pair_sum = num_1 + num_2
        else:
            pair_sum = num_1 + num_2
            value = pair_sum
if con:
    print(f'Yes, value={value}')
elif not con:
    print(f'No, maxdiff={maxdiff}')
