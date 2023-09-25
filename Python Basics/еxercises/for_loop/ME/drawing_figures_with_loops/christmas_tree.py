n = int(input())
counter = 0

for b in range(n, -1, -1):
    for c in range(b):
        print(' ', end='')
    for d in range(counter):
        print('*', end='')
    print(' | ', end='')
    for d in range(counter):
        print('*', end='')
    counter += 1
    print()