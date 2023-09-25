start_number = int(input())
end_number = int(input())

for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        for third_number in range(start_number, end_number + 1):
            for fourth_number in range(start_number, end_number + 1):
                if first_number % 2 == 0 and fourth_number % 2 != 0:
                    if first_number > fourth_number:
                        sum_1 = second_number + third_number
                        if sum_1 % 2 == 0:
                            print(f'{first_number}{second_number}{third_number}{fourth_number}', end=' ')
                elif first_number % 2 != 0 and fourth_number % 2 == 0:
                    if first_number > fourth_number:
                        sum_1 = second_number + third_number
                        if sum_1 % 2 == 0:
                            print(f'{first_number}{second_number}{third_number}{fourth_number}', end=' ')
