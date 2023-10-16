command = ""

while command != "End":
    string_input = input()
    final_result = ""
    if string_input == "SoftUni":
        continue
    elif string_input == "End":
        command = "End"
        break
    else:
        for x in string_input:
            final_result += x*2
    print(final_result)