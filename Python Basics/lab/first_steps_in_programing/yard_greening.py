yard_sqr_meters = float(input())
price_per_sqr_meter = 7.61
price = yard_sqr_meters * price_per_sqr_meter
discount = price * 0.18
final_price = price - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')