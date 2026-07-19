# Sample inputs and outputs
#
# Option 1 — "hello hello world"
#   total characters: 17
#   total words: 3
#   unique words count: 2
#
# Option 2 — "Hello World"
#   upper case: HELLO WORLD
#   lower case: hello world
#   title case: Hello World
#   kebab case: hello-world
#   snake case: hello_world
#
# Option 3 — "1234567890"
#   ******7890
#
# Option 4 — "racecar"
#   text is a palindrome!!!
#
# Option 5 — "ada lovelace"
#   A.L
#
# Empty input for any option:
#   text cannot be empty

menu = """
<<<<Textformatter Pro Max 2000>>>>
    
    Select a functionality:
    1. Get character count, word count and unique word count of any text
    2. Convert text to uppercase, lowercase, title case, snake case and kebab case
    3. Mask sensitive number while preserving the last 4 digits
    4. Check if a text is a palindrome
    5. Generate initials from a full name
    6. Exit
"""

def run_with_text(prompt, action):
    text = input(prompt)
    if not text.strip():
        print('text cannot be empty')
        return
    action(text)

def choice_1(text): 
    char_count = len(text)
    word_count = len(text.split())
    unique_words = {}

    for word in text.split():
        formatted_word = "".join(char for char in word if char.isalnum()).lower()
        if not formatted_word:
            continue

        if not unique_words.get(formatted_word):
            unique_words[formatted_word] = 1
        else:
            unique_words[formatted_word] += 1
    
    print(f'total characters: {char_count}') 
    print(f'total words: {word_count}')
    print(f'unique words count: {len(unique_words)}') 
    

def choice_2(text): 
    upper_case = text.upper()
    lower_case = text.lower()
    title_case = text.title()
    kebab_case = "-".join(text.lower().split())
    snake_case = "_".join(text.lower().split())

    print(f'upper case: {upper_case}')
    print(f'lower case: {lower_case}')
    print(f'title case: {title_case}')
    print(f'kebab case: {kebab_case}')
    print(f'snake case: {snake_case}')

def choice_3(text):
    if len(text) < 4:
        print('number must have at least 4 characters')
        return

    formatted_text = f"{'*' * (len(text) - 4)}{text[-4:]}"
    print(formatted_text)

def choice_4(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    if cleaned == cleaned[::-1]:
        print('text is a palindrome!!!')
    else:
        print('text is not a palindrome!')

def choice_5(text):
    segments = text.split()
    initials = []
    for segment in segments:
        initials.append(segment[0])
    print(".".join(initials).upper())

while True:
    print(menu)
    choice = input('enter your choice: ')

    if choice == '1':
        run_with_text('enter your text: ', choice_1)
    elif choice == '2':
        run_with_text('enter your text: ', choice_2)
    elif choice == '3':
        run_with_text('enter your text: ', choice_3)
    elif choice == '4':
        run_with_text('enter your text: ', choice_4)
    elif choice == '5':
        run_with_text('enter your full name: ', choice_5)
    elif choice == '6':
        exit()
    else:
        print('invalid input')
