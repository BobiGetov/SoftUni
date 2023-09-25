easter_bread_number = int(input())
eggshell_number = int(input())
cookies = int(input())

easter_bread_price = easter_bread_number * 3.20
eggshells_price = eggshell_number * 4.35
cookies_price = cookies * 5.40
eggs_paint_price = eggshell_number * 12 * 0.15

total_price = easter_bread_price + eggshells_price + cookies_price + eggs_paint_price

print(f'{total_price:.2f}')