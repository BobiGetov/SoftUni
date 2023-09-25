pens = int(input())
markers = int(input())
detergent_liters = int(input())
discount = int(input())

pens_price = pens * 5.80
markers_price = markers * 7.20
detergent_liters_price = detergent_liters * 1.20

total_price = pens_price + markers_price + detergent_liters_price
discount_price = total_price - ((total_price*discount)/100)

print(discount_price)
