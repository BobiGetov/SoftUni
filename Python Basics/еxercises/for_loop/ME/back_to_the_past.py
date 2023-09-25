inherited_money = float(input())
end_year = int(input())

money_spent = 0

for i in range(1800, end_year + 1):
    if i % 2 == 0:
        money_spent += 12000
    else:
        age = 18 + (i - 1800)
        money_spent += 12000 + (50 * age)

diff = abs(inherited_money - money_spent)

if money_spent <= inherited_money:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')

elif money_spent > inherited_money:
    print(f'He will need {diff:.2f} dollars to survive.')