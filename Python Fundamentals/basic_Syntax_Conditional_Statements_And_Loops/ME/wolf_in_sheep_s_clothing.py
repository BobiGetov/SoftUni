input_text = input()

input_list = input_text.split(", ")
input_list.reverse()
counter = 0

for index in range(len(input_list)):
    command = input_list[index]
    if command == 'wolf' and counter == 0:
        print("Please go away and stop eating my sheep")
        break
    elif command == 'wolf':
        print(f'Oi! Sheep number {counter}! You are about to be eaten by a wolf!')
        break
    counter += 1