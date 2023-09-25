from math import floor

needed_hours = int(input())
days_to_do = int(input())
workers = int(input())

working_hours = days_to_do * 8
working_hours -= working_hours * 0.10

extra_time = workers * 2 * days_to_do
total_hours =floor(working_hours + extra_time)

diff = abs(total_hours - needed_hours)

if total_hours > needed_hours:
    print(f'Yes!{floor(diff)} hours left.')
elif total_hours < needed_hours:
    print(f'Not enough time!{floor(diff)} hours needed.')
