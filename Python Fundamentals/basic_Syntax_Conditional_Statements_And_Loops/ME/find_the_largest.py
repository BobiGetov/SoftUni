number = int(input())

number = list(str(number))
number = [int(i) for i in number]

number.sort(reverse=True)

for index_number in range(len(number)):
    print(number[index_number], end="")
