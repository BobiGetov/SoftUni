coins_one_bgn = int(input())
coins_two_bgn = int(input())
banknotes_five_bgn = int(input())
amount = int(input())

for a in range(coins_one_bgn + 1):
    n1 = a * 1
    for b in range(coins_two_bgn + 1):
        n2 = b * 2
        for c in range(banknotes_five_bgn + 1):
            n3 = c * 5
            sum = n1 + n2 + n3
            if sum == amount:
                print(f'{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {sum} lv.')
