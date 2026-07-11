username = input('please enter your name: ')
distance = float(input('enter the distance to your destination in km: '))
speed = float(input('enter the speed at which you are traveling to your destination: '))
file_size = float(input('enter the size of the file of your work project in mb: '))
download_speed = float(input('enter the downlad speed of your file in mbps: '))
bill_amount = float(input('enter the bill amount for your restaurant bill: '))
tip = float(input('enter the tip amount you gave to the server: '))

travel_time_in_hours = distance // speed
travel_time_in_minutes = distance % speed

download_time_in_minutes = file_size // download_speed
download_time_in_seconds = file_size % download_speed

total_bill = bill_amount + (bill_amount * (tip/100))
print(f"Hello, {username}!")
print(f'Your travel time is, {travel_time_in_hours} hours and {travel_time_in_minutes} minutes')
print(f"Your download time is, {download_time_in_minutes} minutes and {download_time_in_seconds} seconds")

print("Here is your expenditures")
print(f"{"-"*30}")
print(f"{"subtotal":<12}${bill_amount}")
print(f"{"tip":<12}${tip}")
print(f"{"-"*30}")
print(f"{"total":<12}${total_bill}")

print(f"{"-"*3} Trip Summary {"-"*3}")
print(f"Travel: {travel_time_in_hours} hours and {travel_time_in_minutes} minutes")
print(f"Downloaded: {download_time_in_minutes} minutes and {download_time_in_seconds} seconds")
print(f"Dinner total: ${total_bill}")


