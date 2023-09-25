processor_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_number = int(input())
discount = float(input())

ram_price_in_dollars = ram_number * ram_price
vc_discount_in_dollars = video_card_price - (video_card_price * discount)
pr_discount_in_dollars = processor_price - (processor_price * discount)

total_price_in_dollars = ram_price_in_dollars + vc_discount_in_dollars + pr_discount_in_dollars
total_price_in_bgn = total_price_in_dollars * 1.57

print(f'Money needed - {total_price_in_bgn:.2f} leva.')
