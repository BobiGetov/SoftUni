age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print(f'Mr')
    else:
        print(f'Master')
elif gender == 'f':
    if age >= 16 :
        print(f'Ms.')
    else:
        print(f'Miss')
