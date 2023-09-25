steps = 0
total_steps = 0
condition = True

while True:
    steps = input()

    if steps == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home

        if total_steps >=10000:
            condition = False
        break

    counter = int(steps)
    total_steps += counter

    if total_steps >= 10000:
        condition = False
        break

diff = abs(10000 - total_steps)

if not condition:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')