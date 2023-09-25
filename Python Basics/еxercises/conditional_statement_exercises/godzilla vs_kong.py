film_budget = float(input())
extras = int(input())
price_for_clothes_one_extra = float(input())

decor = film_budget * 0.10
clothes = price_for_clothes_one_extra * extras

if extras >= 150:
    clothes -= clothes * 0.10

total_cost = decor + clothes

diff = abs(film_budget - total_cost)

if total_cost > film_budget:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
elif total_cost <= film_budget:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
