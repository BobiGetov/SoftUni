budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

videocard_price = number_of_videocards * 250
processor_price = number_of_processors * (videocard_price * .35)
ram_price = number_of_ram * (videocard_price * 0.10)

total_price = videocard_price + processor_price + ram_price

if number_of_videocards > number_of_processors:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
elif budget < total_price:
    print(f'Not enough money! You need {diff:.2f} leva more!')