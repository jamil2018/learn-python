sentence = input('enter your sentence: ')

sentence_array = sentence.split(" ")

banned_words = ['hell', 'damn', 'evil']

for i, word in enumerate(sentence_array):
    for banned in banned_words:
        if banned in word:
            word = word.replace(banned, "*" * len(banned))
    sentence_array[i] = word

formatted_sentence = " ".join(sentence_array)

print(formatted_sentence)