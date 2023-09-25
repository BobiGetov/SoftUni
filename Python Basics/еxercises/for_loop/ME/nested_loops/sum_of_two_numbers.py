start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
flag = 0
for a in range(start, end + 1):
    if flag == 1:
        break

    for b in range(start, end + 1):
        counter += 1
        if a + b == magic_number:
            flag = 1
            print(f'Combination N:{counter} ({a} + {b} = {a+b})')

if flag != 1:
    print(f'{counter} combinations - neither equals {magic_number}')