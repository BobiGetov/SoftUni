celsius_degrees = float(input())

fahrenheit_degrees = (celsius_degrees * (9/5))+32
fahrenheit_degrees_formatted = "{:.2f}".format(fahrenheit_degrees)

print(fahrenheit_degrees_formatted)