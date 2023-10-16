n = int(input())

for num in range(1,n+1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        digit = digits % 10
        digits = digits // 10
        sum_of_digits += digit
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')