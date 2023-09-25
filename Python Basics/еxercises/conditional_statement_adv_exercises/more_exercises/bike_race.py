juniors = int(input())
seniors = int(input())
trace_type = input()

junior_fee = 0
senior_fee = 0

if trace_type == 'trail':
    junior_fee = juniors * 5.50
    senior_fee = seniors * 7
elif trace_type == 'cross-country':
    junior_fee = juniors * 8
    senior_fee = seniors * 9.50
elif trace_type == 'downhill':
    junior_fee = juniors * 12.25
    senior_fee = seniors * 13.75
elif trace_type == 'road':
    junior_fee = juniors * 20
    senior_fee = seniors * 21.50

total_fees = junior_fee + senior_fee

if trace_type == 'cross-country' and juniors + seniors >= 50:
    total_fees -= total_fees * 0.25

costs = total_fees - (total_fees * 0.05)

print(f'{costs:.2f}')