text = input('enter your text: ')

words_count = {}

words = text.split(" ")

for word in words:
    formatted_word = "".join(c for c in word if c.isalpha())
    if formatted_word.isalpha():
        words_count[formatted_word] = words_count.get(formatted_word, 0) + 1

print(words_count)