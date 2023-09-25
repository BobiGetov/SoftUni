projection = input()
rows = int(input())
cols = int(input())
ticket_price = 0

if projection == 'Premiere':
    ticket_price = 12.00
elif projection == 'Normal':
    ticket_price = 7.50
elif projection == 'Discount':
    ticket_price = 5.00

full_saloon = rows * cols * ticket_price

print(f'{full_saloon:.2f}')