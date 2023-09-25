degrees = int(input())
day_hour = input()

outfit = 0
shoes = 0

if 10 <= degrees <= 18:
    if day_hour == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_hour == 'Afternoon' or day_hour == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif 18 < degrees <= 24:
    if day_hour == 'Morning' or day_hour == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_hour == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if day_hour == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_hour == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_hour == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
