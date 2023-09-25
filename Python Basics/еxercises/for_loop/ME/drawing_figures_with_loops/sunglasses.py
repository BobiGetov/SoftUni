n = int(input())

for a in range(n * 2):
    print('*', end='')
for b in range(n):
    print(' ', end='')
for c in range(n * 2):
    print('*', end='')
print()
for middle in range(n - 2):
    print('*', end='')
    for d in range(2 * n - 2):
        print('/', end='')
    print('*', end='')
    if int((n - 1) / 2 - 1) == middle:
        for e in range(n):
            print('|', end='')
    else:
        for e in range(n):
            print(' ', end='')
    print('*', end='')
    for d in range(2 * n - 2):
        print('/', end='')
    print('*', end='')
    print()

for e in range(n * 2):
    print('*', end='')
for f in range(n):
    print(' ', end='')
for g in range(n * 2):
    print('*', end='')