text = input('enter your text: ')

words = text.split()

longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"longest word: {longest_word}. length: {len(longest_word)}")