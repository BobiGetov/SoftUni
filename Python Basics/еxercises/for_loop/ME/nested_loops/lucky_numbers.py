n = int(input())

n1, n2, n3, n4 = 0, 0, 0, 0

# fn, sn , tn, fon - first, second, third, fourth number
for fn in range(1, 10):
    n1 = fn
    for sn in range(1, 10):
        n2 = sn
        for tn in range(1, 10):
            n3 = tn
            for fon in range(1, 10):
                n4 = fon
                sum_1 = n1 + n2
                sum_2 = n3 + n4
                if sum_1 == sum_2 and n % sum_1 == 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')