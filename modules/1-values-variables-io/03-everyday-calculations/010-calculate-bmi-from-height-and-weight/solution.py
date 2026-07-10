height = float(input('enter height in meters: '))
weight = float(input('enter weight in kilograms: '))

bmi = weight / (height ** 2)

print(f'your bmi is: {bmi:.2f}')