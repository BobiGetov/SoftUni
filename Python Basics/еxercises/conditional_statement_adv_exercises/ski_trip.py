days_to_stay = int(input()) - 1
type_of_room = input()
rate = input()
room_price = 0

if type_of_room == 'room for one person':
    room_price = 18

elif type_of_room == 'apartment':
    room_price = 25
    if days_to_stay < 10:
        room_price -= room_price * 0.30
    elif 10 <= days_to_stay <= 15:
        room_price -= room_price * 0.35
    elif 15 < room_price:
        room_price -= room_price * 0.50

elif type_of_room == 'president apartment':
    room_price = 35
    if days_to_stay < 10:
        room_price -= room_price * 0.10
    elif 10 <= days_to_stay <= 15:
        room_price -= room_price * 0.15
    elif 15 < room_price:
        room_price -= room_price * 0.20

total_sum = days_to_stay * room_price

if rate == 'positive':
    total_sum += total_sum * 0.25
elif rate == 'negative':
    total_sum -= total_sum * 0.10

print(f'{total_sum:.02f}')

