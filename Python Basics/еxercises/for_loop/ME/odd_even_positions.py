from sys import maxsize

n = int(input())

oddsum = 0
oddnum = 0
oddmin = maxsize
oddmax = -maxsize
evensum = 0
evennum = 0
evenmin = maxsize
evenmax = -maxsize

for i in range(1, n + 1):
    if i % 2 == 0:
        num = float(input())
        evensum += num

        if num >= evenmax:
            evenmax = num

        if num <= evenmin:
            evenmin = num

    else:
        num = float(input())

        oddsum += num

        if num >= oddmax:
            oddmax = num

        if num <= oddmin:
            oddmin = num

print(f'OddSum={oddsum:.2f},')

print("OddMin=", end='')
if oddmin == maxsize:
    print('No,')
else:
    print(f'{oddmin:.2f},')

print(f'OddMax=', end='')
if oddmax == -maxsize:
    print('No,')
else:
    print(f'{oddmax:.2f},')

print(f'EvenSum={evensum:.2f},')

print(f'EvenMin=', end='')
if evenmin == maxsize:
    print('No,')
else:
    print(f'{evenmin:.2f},')

print(f'EvenMax=', end='')
if evenmax == -maxsize:
    print('No')
else:
    print(f'{evenmax:.2f}')