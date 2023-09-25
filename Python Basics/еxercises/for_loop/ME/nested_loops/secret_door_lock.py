top_of_hundreds = int(input())
top_of_tens = int(input())
top_of_ones = int(input())

for hundreds in range(1, top_of_hundreds + 1):
    if hundreds % 2 == 0:
        for tens in range(2, 7 + 1):
            count = 0
            for i in range(2, tens // 2 + 1):
                if tens % i == 0:
                    count += 1
                    break
            if count == 0 and tens <= top_of_tens:
                for ones in range(1, top_of_ones + 1):
                    if ones % 2 == 0:
                        print(f'{hundreds} {tens} {ones}')
