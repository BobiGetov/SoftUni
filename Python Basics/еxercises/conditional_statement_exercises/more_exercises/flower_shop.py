from math import  floor , ceil
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.50
cacti_price = cacti * 8

total_sum = magnolias_price + hyacinths_price + roses_price + cacti_price
total_sum -= total_sum * 0.05

diff = abs(total_sum - gift_price)

if gift_price <= total_sum:
    print(f'She is left with {floor(diff)} leva.')
elif gift_price > total_sum:
    print(f'She will have to borrow {ceil(diff)} leva.')