number = int(input())

p1, p2, p3 = 0, 0, 0

for n in range(1, number + 1):
    numbers = int(input())

    if numbers % 2 == 0:
        p1+=1

    if numbers % 3 == 0:
        p2+=1

    if numbers % 4 == 0:
        p3 +=1

print(f'{p1 / number * 100:.2f}%')
print(f'{p2 / number * 100:.2f}%')
print(f'{p3 / number * 100:.2f}%')