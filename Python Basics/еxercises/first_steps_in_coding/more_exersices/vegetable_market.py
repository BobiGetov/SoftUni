vegetables_price_per_kilo = float(input())
fruit_price_per_kilo = float(input())
vegetables_kilos = int(input())
fruit_kilos = int(input())

total_vegetables = vegetables_kilos * vegetables_price_per_kilo
total_fruits = fruit_kilos * fruit_price_per_kilo

total_sum =(total_fruits + total_vegetables)/1.94
total_sum_formatted = "{:.2f}".format(total_sum)

print(total_sum_formatted)