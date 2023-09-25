deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

interest = deposit_amount * annual_interest_rate / 100
month_interest_rate = interest / 12
total_sum = deposit_amount + deposit_term*month_interest_rate

print(total_sum)