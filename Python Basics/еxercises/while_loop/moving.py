free_space_width = int(input()) * 10
free_space_length = int(input()) * 10
free_space_height = int(input()) * 10

free_space_cubic_area = int(free_space_width * free_space_length * free_space_height / 1000)
total_boxes = 0
remaining_space = 0
counter = 0
condition = True

while True:
    current_boxes = input()

    if current_boxes == 'Done':
        condition = False
        break

    counter = int(current_boxes)
    total_boxes += counter
    remaining_space = free_space_cubic_area - total_boxes

    if remaining_space <= 0:
        remaining_space = abs(remaining_space)
        break

if not condition:
    print(f'{remaining_space} Cubic meters left.')
else:
    print(f'No more free space! You need {remaining_space} Cubic meters more.')
