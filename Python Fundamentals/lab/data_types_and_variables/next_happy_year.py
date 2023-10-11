current_year = int(input())

command = True

while command:
    year_list = list(str(current_year))
    year_list_int = [int(x) for x in year_list]
    happy_year = []
    counter = 0
    for a in year_list_int:
        if a in happy_year:
            current_year += 1
            break
        else:
            happy_year.append(a)
            counter += 1
    if counter == len(year_list_int):
        happy_year = [str(x) for x in happy_year]
        command = False

result = int(''.join(happy_year))

print(result)
