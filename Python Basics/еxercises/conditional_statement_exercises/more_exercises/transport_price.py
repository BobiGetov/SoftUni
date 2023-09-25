km = int(input())
trip_status = input()

taxi_price = 0

if trip_status == 'day':
    taxi_price = 0.79 * km + 0.70
elif trip_status == 'night':
    taxi_price = 0.90 * km + 0.70

if km < 20:
    print(f'{taxi_price:.2f}')

elif 20 <= km < 100:
    bus_price = 0.09 * km
    print(f'{bus_price:.2f}')
elif 100 <= km:
    train_price = 0.06 * km
    print(f'{train_price:.2f}')
