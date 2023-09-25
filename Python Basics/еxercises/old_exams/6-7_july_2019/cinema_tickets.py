students_tickets = 0
standard_tickets = 0
kid_tickets = 0
condition = False
while True:
    movie_name = input()

    if movie_name == 'Finish':
        condition = True
        break
    else:
        free_seats = int(input())
        stud_counter = 0
        stand_counter = 0
        kid_counter = 0

        for row in range(free_seats):
            ticket_type = input()

            if ticket_type == 'student':
                students_tickets += 1
                stud_counter += 1

            elif ticket_type == 'standard':
                standard_tickets += 1
                stand_counter += 1

            elif ticket_type == 'kid':
                kid_tickets += 1
                kid_counter += 1

            elif ticket_type == 'End':
                break
        total_sell_tickets = kid_counter + stand_counter + stud_counter
        print(f'{movie_name} - {total_sell_tickets / free_seats * 100:.2f}% full.')

total_tickets = kid_tickets + standard_tickets + students_tickets

if condition:
    print(f'Total tickets: {total_tickets}')
    print(f'{students_tickets / total_tickets * 100:.2f}% student tickets.')
    print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
    print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
