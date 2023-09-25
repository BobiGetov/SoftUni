n = int(input())

roof_rows = int((n + 1) / 2)
body_rows = int(n / 2)
flag = 0
r = '*'
a = 0
counter = 0

for roof in range(roof_rows, 0, -1):

    # first row
    if flag == 0:

        while counter != (roof - 1):
            print('-', end='')
            counter += 1

        if n % 2 == 0:
            print('**', end='')
            a = 2

        elif n % 2 != 0:
            print('*', end='')
            a = 1

        while counter != 0:
            print('-', end='')
            counter -= 1

        print()

    # every next row

    if flag >= 1:
        a += 2

        while counter != (roof - 1):
            print('-', end='')
            counter += 1

        print(r * a, end='')

        while counter != 0:
            print('-', end='')
            counter -= 1
        print()

    flag += 1

for body in range(body_rows):
    print('|', end='')
    print('*' * (n - 2), end='')
    print('|')
