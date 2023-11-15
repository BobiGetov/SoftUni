input_word = list(str.lower(input()))

word_to_compare = ""
counter = 0
number_of_loops = 0

while len(input_word) != number_of_loops:
    for index in range(number_of_loops,len(input_word),1):
        index_word = input_word[index]
        word_to_compare += index_word

        if word_to_compare == "water" or word_to_compare == "fish" or word_to_compare == "sun" or word_to_compare == "sand":
            counter += 1
            number_of_loops += 1
            word_to_compare = ""
            break
        elif index == len(input_word)-1:
            number_of_loops += 1
            word_to_compare = ""
            break

print(counter)