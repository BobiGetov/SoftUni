first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

first_pair_end = first_pair_start + first_pair_diff
second_pair_end = second_pair_start + second_pair_diff

for a in range(first_pair_start, first_pair_end + 1):
    count = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            count += 1
            break
    if count == 0 and a <= first_pair_end:
        for b in range(second_pair_start, second_pair_end + 1):
            count = 0
            for i in range(2, b // 2 + 1):
                if b % i == 0:
                    count += 1
                    break
            if count == 0 and b <= second_pair_end:
                print(f'{a}{b}')

