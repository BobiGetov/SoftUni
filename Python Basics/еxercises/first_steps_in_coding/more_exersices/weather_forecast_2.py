temp = float(input())

if 26 <= temp <= 35:
    print(f'Hot')
elif 20<temp<26:
    print(f'Warm')
elif 15<=temp<=20:
    print(f'Mild')
elif 12<=temp<15:
    print(f'Cool')
elif 5 <= temp < 12:
    print(f'Cold')
else:
    print(f'unknown')