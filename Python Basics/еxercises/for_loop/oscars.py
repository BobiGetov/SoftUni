name_of_actor = input()
points_from_academy = float(input())
number_of_jury = int(input())

condition = True

for _ in range(number_of_jury):
    judge_name = input()
    judge_points = float(input())

    points_from_academy = points_from_academy + ((len(judge_name) * judge_points) / 2)

    if points_from_academy >= 1250.5:
        condition = False
        break

if not condition:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {points_from_academy:.1f}!')
elif points_from_academy < 1250.5:
    diff = abs(points_from_academy - 1250.5)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')