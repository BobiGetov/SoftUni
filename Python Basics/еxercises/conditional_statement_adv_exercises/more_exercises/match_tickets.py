budget = float(input())
category = input()
group_number = int(input())

ticket_price = 0

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

if 1 <= group_number <= 4:
    budget -= budget * 0.75
elif 4 < group_number <= 9:
    budget -= budget * 0.60
elif 9 < group_number <= 24:
    budget -= budget * 0.50
elif 24 < group_number <= 49:
    budget -= budget * 0.40
elif group_number >= 50:
    budget -= budget * 0.25

group_tickets_price = group_number * ticket_price

diff = abs(group_tickets_price - budget)

if budget >= group_tickets_price:
    print(f'Yes! You have {diff:.2f} leva left.')

elif budget < group_tickets_price:
    print(f'Not enough money! You need {diff:.2f} leva.')