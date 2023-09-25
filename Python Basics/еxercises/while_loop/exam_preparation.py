bad_grades = int(input())

bad_grades_counter = 0
total_grade_sum = 0
tasks_counter = 0
task_name = ''

while True:
    cur_task_name = input()

    if cur_task_name == 'Enough':
        print(f'Average score: {total_grade_sum / tasks_counter:.2f}')
        print(f'Number of problems: {tasks_counter}')
        print(f'Last problem: {task_name}')
        break

    grade = int(input())

    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades:
            print(f'You need a break, {bad_grades_counter} poor grades.')
            break
    task_name = cur_task_name
    tasks_counter += 1
    total_grade_sum += grade

