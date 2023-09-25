men_number = int(input())
women_number = int(input())
max_tables = int(input())

counter = 0

for ft in range(1, men_number+1):
    if counter == max_tables:
        break
    for st in range(1, women_number + 1):
        print(f'({ft} <-> {st})', end=' ')
        counter += 1
        if counter == max_tables:
            break