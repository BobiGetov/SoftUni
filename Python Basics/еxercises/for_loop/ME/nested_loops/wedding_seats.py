last_sector = input()
rows_in_first_sector = int(input())
seats_in_odd_row = int(input())

first_sector = ord('A')
last_sector = ord(last_sector)
seat = ord('dash')
seats_counter = 0

for sectors in range(first_sector, last_sector + 1):
    for rows in range(1, rows_in_first_sector + 1):
        seat = ord('dash')
        if rows % 2 != 0:
            for seats in range(1, seats_in_odd_row + 1):
                print(f'{chr(sectors)}{rows}{chr(seat)}')
                seat += 1
                seats_counter +=1
        elif rows % 2 == 0:
            for seats in range(1, seats_in_odd_row + 3):
                print(f'{chr(sectors)}{rows}{chr(seat)}')
                seat += 1
                seats_counter += 1
    rows_in_first_sector += 1
print(seats_counter)