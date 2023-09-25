row_1 = input()
row_2 = input()
row_3 = input()

counter = 0
letter_start = ord(row_1)
letter_stop = ord(row_2)
skipped_letter = ord(row_3)

for a in range(letter_start, letter_stop + 1):
    if skipped_letter != a:
        for b in range(letter_start, letter_stop + 1):
            if skipped_letter != b:
                for c in range(letter_start, letter_stop + 1):
                    if skipped_letter != c:
                        counter += 1
                        print(f'{chr(a)}{chr(b)}{chr(c)}', end=' ')
print(counter)
