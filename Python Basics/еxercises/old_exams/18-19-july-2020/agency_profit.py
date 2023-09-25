company_name = input()
adult_tickets = int(input())
children_tickets = int(input())
ticket_price = float(input())
service_fee = float(input())

children_tickets_price = children_tickets * (ticket_price * 0.3)
adult_tickets_price = adult_tickets * ticket_price
service_fee_price = (adult_tickets + children_tickets) * service_fee

total_ticket_price = children_tickets_price + adult_tickets_price + service_fee_price

agency_profit = total_ticket_price * 0.20

print(f'The profit of your agency from {company_name} tickets is {agency_profit:.2f} lv.')