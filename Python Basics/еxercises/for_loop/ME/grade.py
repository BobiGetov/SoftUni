number_of_students = int(input())

fail, medium, good, excellent = 0, 0, 0, 0
total_sum_grades = 0

for _ in range(number_of_students):
    current_grade = float(input())
    total_sum_grades += current_grade

    if 2 <= current_grade < 3:
        fail += 1

    elif 3 <= current_grade < 4:
        medium += 1

    elif 4 <= current_grade < 5:
        good += 1

    elif 5 <= current_grade:
        excellent += 1

print(f'Top students: {excellent / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {good / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {medium / number_of_students * 100:.2f}%')
print(f'Fail: {fail / number_of_students * 100:.2f}%')
print(f'Average: {total_sum_grades / number_of_students:.2f}')