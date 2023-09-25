film_name = input()
saloon_name = input()
tickets_number = int(input())

ticket_price = 0

if film_name == 'A Star Is Born':
    if saloon_name == 'normal':
        ticket_price = tickets_number * 7.50
    elif saloon_name == 'luxury':
        ticket_price = tickets_number * 10.50
    elif saloon_name == 'ultra luxury':
        ticket_price = tickets_number * 13.50

elif film_name == 'Bohemian Rhapsody':
    if saloon_name == 'normal':
        ticket_price = tickets_number * 7.35
    elif saloon_name == 'luxury':
        ticket_price = tickets_number * 9.45
    elif saloon_name == 'ultra luxury':
        ticket_price = tickets_number * 12.75

elif film_name == 'Green Book':
    if saloon_name == 'normal':
        ticket_price = tickets_number * 8.15
    elif saloon_name == 'luxury':
        ticket_price = tickets_number * 10.25
    elif saloon_name == 'ultra luxury':
        ticket_price = tickets_number * 13.25

elif film_name == 'The Favourite':
    if saloon_name == 'normal':
        ticket_price = tickets_number * 8.75
    elif saloon_name == 'luxury':
        ticket_price = tickets_number * 11.55
    elif saloon_name == 'ultra luxury':
        ticket_price = tickets_number * 13.95

print(f'{film_name} -> {ticket_price:.2f} lv.')