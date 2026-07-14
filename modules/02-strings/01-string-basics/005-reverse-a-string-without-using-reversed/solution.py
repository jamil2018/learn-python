test_string = input('input your word for palindrome validation: ')

if test_string == test_string[::-1]:
    print('it a palindrome!!')
else:
    print('not a palindrome.')