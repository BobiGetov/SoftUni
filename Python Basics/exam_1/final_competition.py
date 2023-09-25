dancers_number = int(input())
points_number = float(input())
season = input()
place = input()

money_award = 0

if place == 'Bulgaria':
    money_award = points_number * dancers_number
    if season == 'summer':
        money_award -= money_award * 0.05
    elif season == 'winter':
        money_award -= money_award * 0.08

elif place == 'Abroad':
    current_award = dancers_number * points_number
    money_award = current_award + (current_award * 0.50)
    if season == 'summer':
        money_award -= money_award * 0.10
    elif season == 'winter':
        money_award -= money_award * 0.15

charity = money_award * 0.75
money_after_charity = money_award - charity
dancer_money = money_after_charity / dancers_number

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {dancer_money:.2f}')
