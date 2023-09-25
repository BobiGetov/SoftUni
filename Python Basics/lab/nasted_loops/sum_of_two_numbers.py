number1 = int(input())
number2 = int(input())
magic_number = int(input())
counter = 0
current_number1 = 0
current_number2 = 0
flag = False

for a in range(number1, number2 + 1):
    current_number1 = a
    for b in range (number1, number2 + 1):
        current_number2 = b
        counter += 1
        if a+b == magic_number:
            flag = True
            break
    if flag == True:
        break

if flag:
    print(f'Combination N:{counter} ({current_number1} + {current_number2} = {magic_number})')
else:
    print(f'{counter} combinations - neither equals {magic_number}')