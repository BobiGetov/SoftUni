annual_tax_price = int(input())
sneakers = annual_tax_price - ((annual_tax_price*40)/100)
jersey = sneakers - ((sneakers*20)/100)
ball = jersey / 4
accessories = ball / 5

total_equipment_price = annual_tax_price + sneakers + jersey + ball + accessories

print(total_equipment_price)