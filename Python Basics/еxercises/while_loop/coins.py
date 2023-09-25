change_input = int(float(input()) * 100)
number_of_coins = 0

while change_input > 0:
    if change_input >= 200:
        change_input -= 200

    elif change_input >= 100:
        change_input -= 100

    elif change_input >= 50:
        change_input -= 50

    elif change_input >= 20:
        change_input -= 20

    elif change_input >= 10:
        change_input -= 10

    elif change_input >= 5:
        change_input -= 5

    elif change_input >= 2:
        change_input -= 2

    elif change_input >= 1:
        change_input -= 1

    number_of_coins += 1

print(number_of_coins)