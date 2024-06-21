user_input = input("Text: ")
text = sorted(user_input.split(" "))
word_count = {}
length_of_word = 0
for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    if length_of_word < len(word):
        length_of_word = len(word)
for word in word_count:
    print(f"{word:{length_of_word}} = {word_count[word]}")

