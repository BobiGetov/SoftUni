n2_top = int(input())

for n2 in range(2, n2_top + 1):
    count = 0
    for i in range(2, n2 // 2 + 1):
        if n2 % i == 0:
            count += 1
            break
    if count == 0 and n2 <= n2_top:
        print(n2)