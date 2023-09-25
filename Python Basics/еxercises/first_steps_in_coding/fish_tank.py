length =int(input())
width =int(input())
height =int(input())
percent_occupied_space =float(input())

aquarium_volume = length * width * height
liters = aquarium_volume / 1000
needed_liters = liters * (1-0.17)

print(needed_liters)