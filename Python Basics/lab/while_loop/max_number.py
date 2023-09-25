from sys import maxsize

max_num = - maxsize

while True:
    number = input()

    if number == 'Stop':
        break

    number = int(number)

    if max_num <= number:
        max_num = number

print(max_num)