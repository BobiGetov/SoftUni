name = input()
excl = 0
counter = 0
total_sum = 0
con = False

while counter < 12:
    grade = float(input())

    if grade < 4:
        excl += 1
        if excl > 1:
            counter += 1
            con = True
            break

    else:
        total_sum += grade
        counter += 1
if con:
    print(f'{name} has been excluded at {counter} grade')
else:
    total_sum /= counter
    print(f'{name} graduated. Average grade: {total_sum:.2f}')