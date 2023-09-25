nylon = int(input())
paint_liters = int(input())
razr_liters = int(input())
work_hours = int(input())

nylon_price = (nylon+2) * 1.50
paint_price = (paint_liters+(paint_liters*10/100)) * 14.50
razr_price = razr_liters * 5

materials_price = nylon_price + paint_price + razr_price + 0.40

work_price = ((materials_price * 30) / 100) * work_hours

total_price = work_price + materials_price

print(total_price)