number = int(input())

for i in range(number):
    msg_number = int(input())
    if msg_number == 88:
        print("Hello")
    elif msg_number == 86:
        print("How are you?")
    elif msg_number < 88:
        print("GREAT!")
    elif msg_number > 88:
        print("Bye.")