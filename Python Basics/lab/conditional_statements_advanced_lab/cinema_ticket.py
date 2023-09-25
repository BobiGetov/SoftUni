day_of_week = input()

if day_of_week in 'Monday Tuesday Friday':
    print(f'12')
elif day_of_week in 'Wednesday Thursday':
    print(f'14')
elif day_of_week in 'Saturday Sunday':
    print(f'16')