principal = float(input('enter your principal amount: '))
rate = float(input('enter the interest rate: '))/100
time = float(input('enter time period in years: '))

interest = principal * rate * time

print(f'interest amount: {interest}')