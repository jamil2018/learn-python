card_number = input('enter your card number: ')

masked_number = "*" * (len(card_number) - 4) + card_number[-4:]

print(f'your masked card number: {masked_number}')