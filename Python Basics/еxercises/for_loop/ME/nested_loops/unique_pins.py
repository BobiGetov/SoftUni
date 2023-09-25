n1_top = int(input())
n2_top = int(input())
n3_top = int(input())

for n1 in range(1, n1_top + 1):
    if n1 % 2 == 0:

        for n2 in range(2, 7 + 1):
            count = 0
            for i in range(2, n2 // 2 + 1):
                if n2 % i == 0:
                    count += 1
                    break
            if count == 0 and n2 <= n2_top:
                for n3 in range(1, n3_top + 1):
                    if n3 % 2 == 0:
                        print(f'{n1} {n2} {n3}')
