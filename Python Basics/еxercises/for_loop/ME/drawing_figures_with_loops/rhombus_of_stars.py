n = int(input())

for a in range(1, n):
    for b in range(n-a):
        print(' ', end='')
    print('*', end='')
    for c in range(a-1):
        print(' *', end='')
    print()
for d in range(1, n + 1):
    for f in range(d - 1):
        print(' ', end='')
    for e in range(n - d):
        print('* ', end='')
    print('*', end='')
    print('')
