chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegan_menu_price = vegan_menu * 8.15
total_menu_price = chicken_menu_price + fish_menu_price + vegan_menu_price
desert_price = total_menu_price * 0.2

total_order_price = total_menu_price + desert_price + 2.5

print(total_order_price)