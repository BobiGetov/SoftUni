n = int(input())

for strings in range(n):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(string, "is not pure!")
    else:
        print(string, "is pure.")