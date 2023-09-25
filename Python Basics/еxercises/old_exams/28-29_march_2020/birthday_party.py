hall_rent = int(input())

cake = hall_rent * 0.20
drinks = cake -(cake * 0.45)
animator = hall_rent / 3

needed_budget = cake + drinks + animator + hall_rent

print(needed_budget)