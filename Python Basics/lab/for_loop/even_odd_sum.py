n = int(input())

odd_sum = 0
even_sum = 0

for i in range(n):
    if i % 2 == 0:
        odd_sum += int(input())
    else:
        even_sum += int(input())

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff= abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')