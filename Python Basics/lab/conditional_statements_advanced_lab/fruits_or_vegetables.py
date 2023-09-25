product_name = input()

if product_name in 'banana apple kiwi cherry lemon grapes':
    print(f'fruit')
elif product_name in 'tomato cucumber pepper carrot':
    print(f'vegetable')
else:
    print(f'unknown')