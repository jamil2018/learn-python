bill_amount = float(input('enter total bill: '))
tip_percentage = float(input('enter tip percentage: '))

total_bill = bill_amount + (bill_amount * (tip_percentage/100))

print(f'total bill: {total_bill}')