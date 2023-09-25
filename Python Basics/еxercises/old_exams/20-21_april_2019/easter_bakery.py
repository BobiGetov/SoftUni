flour_price_per_kilo = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
eggshell_number = int(input())
yeast_packets = int(input())

sugar_price = flour_price_per_kilo * 0.75
eggshell_price = flour_price_per_kilo * 1.10
yeast_price = sugar_price * 0.20

total_flour_price = flour_price_per_kilo * flour_kilos
total_eggshell_price = eggshell_number * eggshell_price
total_sugar_price = sugar_kilos * sugar_price
total_yeast_price = yeast_packets * yeast_price

total_price = total_yeast_price + total_sugar_price + total_eggshell_price + total_flour_price

print(f'{total_price:.2f}')