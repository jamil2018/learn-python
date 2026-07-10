from datetime import datetime


birth_year = int(input('enter your birth year: '))

age = datetime.now().year - birth_year

print(f'your estimated age: {age}')