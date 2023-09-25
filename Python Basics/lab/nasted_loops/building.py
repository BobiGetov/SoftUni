floors = int(input())
rooms = int(input())

for last_floor in range(0,rooms):
    print(f'L{floors}{last_floor}', end=' ')
print(end='\n')
for floor in range(floors - 1, 0, -1):
    if floor % 2 == 0:
        for floor_rooms in range(rooms):
            print(f'O{floor}{floor_rooms}', end=' ')
        print(end='\n')
    else:
        for floor_rooms in range(rooms):
            print(f'A{floor}{floor_rooms}', end=' ')
        print(end='\n')
