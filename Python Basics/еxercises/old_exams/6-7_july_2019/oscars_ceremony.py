hall_rent = int(input())

statuette = hall_rent - (hall_rent * 0.30)
catering = statuette - (statuette * 0.15)
sound = catering * 0.50

total_price = statuette + catering + sound + hall_rent

print(f'{total_price:.2f}')