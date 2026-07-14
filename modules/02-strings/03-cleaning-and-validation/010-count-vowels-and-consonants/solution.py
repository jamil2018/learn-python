word = input('enter your word: ').lower()
vowels = 'aeiou'

vowel_counter = 0
consonant_counter = 0

for letter in word:
    if letter in vowels:
        vowel_counter+=1
    else:
        consonant_counter+=1

print(f"vowels: {vowel_counter} consonants: {consonant_counter}")