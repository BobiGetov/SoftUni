holidays = int(input())

tom_play_per_year = 30000

working_days = (365 - holidays)

when_work = working_days * 63
when_holiday = holidays * 127
total_play_minutes = when_holiday + when_work

diff = abs(total_play_minutes - tom_play_per_year)

hour = diff // 60
minutes = diff % 60

if tom_play_per_year >= total_play_minutes:
    print('Tom sleeps well')
    print(f'{hour} hours and {minutes:02d} minutes less for play')

elif tom_play_per_year < total_play_minutes:
    print('Tom will run away')
    print(f'{hour} hours and {minutes:02d} minutes more for play')
