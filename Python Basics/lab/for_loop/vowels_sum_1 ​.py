text = input()
number = 0
total_sum = 0
for ch in text:
    if ch == 'dash':
        number = 1
    elif ch == 'e':
        number = 2
    elif ch == 'i':
        number = 3
    elif ch == 'o':
        number = 4
    elif ch == 'u':
        number = 5
    else:
        number = 0
    total_sum += number

print(total_sum)
