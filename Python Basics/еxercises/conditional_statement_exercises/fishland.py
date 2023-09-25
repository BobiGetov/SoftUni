mackerel_price_per_kilo = float(input())
sprat_price_per_kilo = float(input())
bonito_kilos = float(input())
scad_kilos = float(input())
shell_kilos = int(input())

bonito_price = bonito_kilos * (mackerel_price_per_kilo * 1.60)
scad_price = scad_kilos * (sprat_price_per_kilo * 1.8)
shell_price = shell_kilos * 7.50

total_sum = bonito_price + scad_price + shell_price

print(f'{total_sum:.02f}')