name = input('enter your full name: ')
initials = []

for name_part in name.split(): 
    initials.append(name_part[0])

print(f'your initials are: {".".join(initials).upper()}')