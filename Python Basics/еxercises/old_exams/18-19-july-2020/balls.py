from math import floor

number = int(input())

total_points = 0
red_balls, orange_balls, yellow_balls, white_balls, black_balls, other_balls = 0, 0, 0, 0, 0, 0

for _ in range(number):
    ball_color = input()

    if ball_color == 'red':
        total_points += 5
        red_balls += 1

    elif ball_color == 'orange':
        total_points += 10
        orange_balls += 1

    elif ball_color == 'yellow':
        total_points += 15
        yellow_balls += 1

    elif ball_color == 'white':
        total_points += 20
        white_balls += 1

    elif ball_color == 'black':
        total_points = floor(total_points / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f'Total points: {total_points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_balls}')