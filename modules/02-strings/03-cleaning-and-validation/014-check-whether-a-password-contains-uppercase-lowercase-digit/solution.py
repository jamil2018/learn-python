from tokenize import String

def validate_password(password:String):
    uppercase_char_count = 0
    lowercase_char_count = 0
    digit_count = 0
    symbol_count = 0
    errors = []

    for c in password:
        if c.isupper():
            uppercase_char_count += 1
        elif c.islower():
            lowercase_char_count += 1
        elif c.isdigit():
            digit_count += 1
        elif c in "!@#$%...":
            symbol_count +=1

    if(uppercase_char_count > 0 and lowercase_char_count > 0 and digit_count > 0 and symbol_count > 0):
        print('valid password')
        return
    if uppercase_char_count == 0:
        errors.append('password requires at least one upper case letter')
    if lowercase_char_count == 0:
        errors.append('password requires at least one lower case letter')
    if digit_count == 0:
        errors.append('password requires at least one number')
    if symbol_count == 0:
        errors.append('password requires at least one symbol')
    
    print(f"invalid password.\n\nerrors: {", ".join(errors)}")


validate_password(input('enter your password: '))
