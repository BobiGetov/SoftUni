days = int(input())
hours = int(input())

total_price = 0

for d in range(1, days + 1):
    day_price = 0
    for h in range(1, hours + 1):
        if d % 2 == 0:
            if h % 2 != 0:
                day_price += 2.5
                total_price += 2.5
            else:
                day_price += 1
                total_price += 1
        elif d % 2 != 0:
            if h % 2 == 0:
                day_price += 1.25
                total_price += 1.25
            else:
                day_price += 1
                total_price += 1

    print(f'Day: {d} - {day_price:.2f} leva')

print(f'Total: {total_price:.2f} leva')