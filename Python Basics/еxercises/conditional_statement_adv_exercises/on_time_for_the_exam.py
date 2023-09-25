exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_hour_in_minutes = (exam_hour * 60) + exam_minute
arrival_hour_in_minutes = (arrival_hour * 60) + arrival_minute
half_hour_before_exam = exam_hour_in_minutes - 30
diff = abs(arrival_hour_in_minutes - exam_hour_in_minutes)

hour = diff // 60
minutes = diff % 60

if arrival_hour_in_minutes < half_hour_before_exam:
    print('Early')
    if diff <= 59:
        print(f'{minutes} minutes before the start')
    else:
        print(f'{hour}:{minutes:02d} hours before the start')

elif half_hour_before_exam <= arrival_hour_in_minutes <= exam_hour_in_minutes:
    print('On time')
    if diff <= 30:
        print(f'{minutes} minutes before the start')
elif arrival_hour_in_minutes > exam_hour_in_minutes:
    print('Late')
    if diff <= 59:
        print(f'{minutes} minutes after the start')
    else:
        print(f'{hour}:{minutes:02d} hours after the start')
