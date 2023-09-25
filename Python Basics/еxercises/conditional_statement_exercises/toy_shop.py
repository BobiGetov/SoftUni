trip_price = float(input())
puzzles = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

toys_price = (puzzles * 2.60) + (talking_doll * 3) + (teddy_bear * 4.10) + (minions * 8.20) + (trucks * 2)
toys_count = puzzles + talking_doll + teddy_bear + minions + trucks

if toys_count >= 50:
    toys_price -= toys_price * 0.25

shop_rent = toys_price * 0.10
profit = toys_price - shop_rent
money_left = abs(profit - trip_price)

if profit >= trip_price:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')
