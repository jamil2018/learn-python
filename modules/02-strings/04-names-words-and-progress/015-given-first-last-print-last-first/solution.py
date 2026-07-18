full_name = input('please enter your name: ')

formatted_name = ", ".join(reversed(full_name.split(' ')))

print(f'hi {formatted_name}')