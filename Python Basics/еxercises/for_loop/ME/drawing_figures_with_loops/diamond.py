from math import ceil

n = int(input())

counter = 0
flag = 0
dash_condition = True

dash = ceil((n / 2) - 1)
mid_dash = 1
even = False

if n % 2 == 0:
    n -= 1
    even = True
    mid_dash = 2

for rows in range(n, 0, -1):
    # first row
    if flag == 0:
        while counter != dash:
            print('-', end='')
            counter += 1

        if even:
            print('**', end='')
        else:
            print('*', end='')

        while counter != 0:
            print('-', end='')
            counter -= 1
        print()

    if flag >= 1 and rows != 1:
        while counter != dash and dash != 0:
            print('-', end='')
            counter += 1

        print('*', end='')

        print('-' * mid_dash, end='')

        print('*', end='')

        while counter != 0 and dash != 0:
            print('-', end='')
            counter -= 1
        print()

    if rows == 1 and n > 2:
        while counter != dash:
            print('-', end='')
            counter += 1

        if even:
            print('**', end='')
        else:
            print('*', end='')

        while counter != 0:
            print('-', end='')
            counter -= 1

    if dash_condition:
        if dash != 0:
            dash -= 1
            if flag != 0:
                mid_dash += 2
        elif dash == 0:
            dash += 1
            mid_dash -= 2
            dash_condition = False
    elif not dash_condition:
        dash += 1
        mid_dash -= 2

    flag += 1
