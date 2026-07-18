username = input('enter your username: ')

username_length = len(username)
is_alphanumeric = username.isalnum()

if (username_length >= 3 and username_length<=16) and is_alphanumeric:
    print('username is correct')
elif not is_alphanumeric:
    print('username can only contain numbers and letters')
elif username_length<3:
    print('username is too short')
elif username_length>16:
    print('username is too long')
else:
    print(f'unidentified error. input: {username}')


