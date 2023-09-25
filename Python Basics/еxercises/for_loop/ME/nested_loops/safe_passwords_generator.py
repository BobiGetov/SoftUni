a = int(input())
b = int(input())
max_number_passwords = int(input())

# template ABabBA where A is in range 35 - 55 and B is in range 64 - 96

first_symbol = 35
second_symbol = 64
counter = 0

for first_digit in range(1, a + 1):
    for second_digit in range(1, b + 1):
        if first_symbol > 55:
            first_symbol = 35
        if second_symbol > 96:
            second_symbol = 64
        if counter == max_number_passwords:
            break
        print(f'{chr(first_symbol)}{chr(second_symbol)}', end='')
        print(f'{first_digit}{second_digit}', end='')
        print(f'{chr(second_symbol)}{chr(first_symbol)}', end='|')
        first_symbol += 1
        second_symbol += 1
        counter += 1