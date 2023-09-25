number_one = int(input())
number_two = int(input())
operator = input()

result = 0
even_or_odd = ''
condition = True

if number_two == 0:
    print(f'Cannot divide {number_one} by zero')
    condition = False
else:
    if operator == '+':
        result = number_one + number_two
    elif operator == '-':
        result = number_one - number_two
    elif operator == '*':
        result = number_one * number_two
    elif operator == '/':
        result = number_one / number_two
    elif operator == '%':
        result = number_one % number_two

if condition == True:
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

if condition == True:
    if operator in '+ - *':
        print(f'{number_one} {operator} {number_two} = {result} - {even_or_odd}')
    elif operator == '/':
        print(f'{number_one} {operator} {number_two} = {result:.2f}')
    elif operator == '%':
        print(f'{number_one} {operator} {number_two} = {result}')
