m = int(input())

counter = 0
password = ''
flag = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == m and a < b and c > d:
                    counter += 1
                    print(f'{a}{b}{c}{d}', end=' ')
                    if counter == 4:
                        password = f'{a}{b}{c}{d}'
                        flag = 1
print()
if flag == 1:
    print(f'Password: {password}')
elif flag == 0:
    print('No!')
