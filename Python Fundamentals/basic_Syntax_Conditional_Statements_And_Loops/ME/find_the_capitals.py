word = input()
word_list = list(str(word))
index_list =[]

for index in range(len(word)):
    if word_list[index].isupper():
        index_list.append(index)

print(index_list)