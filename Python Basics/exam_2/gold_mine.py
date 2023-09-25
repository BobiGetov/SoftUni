locations = int(input())

for l in range(locations):
    expected_yield = float(input())
    number_of_days = int(input())

    yielded_gold_per_day = 0

    for d in range(number_of_days):
        yielded_gold_per_day += float(input())

    average_yield = yielded_gold_per_day / number_of_days

    if average_yield >= expected_yield:
        print(f'Good job! Average gold per day: {average_yield:.2f}.')

    elif average_yield < expected_yield:
        diff = abs(expected_yield - average_yield)
        print(f'You need {diff:.2f} gold.')