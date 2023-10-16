number_of_orders = int(input())

total_price_of_orders = 0

for orders in range(number_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0 < price <= 100 and 0 < days <= 31 and 0 < capsules <= 2000:
        price_per_order = price * capsules * days
        total_price_of_orders += price_per_order
        print(f"The price for the coffee is: ${price_per_order:.2f}")

if total_price_of_orders ==0:
    pass
else:
    print(f"Total: ${total_price_of_orders:.2f}")