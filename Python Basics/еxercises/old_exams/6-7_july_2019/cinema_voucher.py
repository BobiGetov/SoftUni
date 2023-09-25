voucher_value = int(input())

movie_ticket = 0
other_purchases = 0

while True:
    purchase_name = input()
    ascii_values = [ord(ch) for ch in purchase_name]
    if purchase_name == 'End':
        break

    elif len(purchase_name) > 8:
        purchase_price = ascii_values[0] + ascii_values[1]
        if purchase_price <= voucher_value:
            movie_ticket += 1
        voucher_value -= purchase_price
    elif len(purchase_name) <= 8:
        purchase_price = ascii_values[0]
        if purchase_price <= voucher_value:
            other_purchases += 1
        voucher_value -= purchase_price
    if voucher_value <= 0:
        break

print(f'{movie_ticket}')
print(f'{other_purchases}')
