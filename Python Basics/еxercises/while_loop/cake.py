cake_width = int(input()) * 10
cake_length = int(input()) * 10

cake_area = cake_width * cake_length
cake_pieces = int(cake_area / 100)
counter = 0
sum_take_pieces = 0
current_pieces = 0
condition = True

while True:
    take_pieces = input()

    if take_pieces == 'STOP':
        condition = False
        break

    counter = int(take_pieces)

    sum_take_pieces += counter
    current_pieces = cake_pieces - sum_take_pieces

    if current_pieces <= 0:
        current_pieces = abs(current_pieces)
        break

if not condition:
    print(f'{current_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {current_pieces} pieces more.')
