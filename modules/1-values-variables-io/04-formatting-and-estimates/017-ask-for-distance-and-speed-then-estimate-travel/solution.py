distance = float(input('enter the distance to destination from current location in kilometers: '))
speed = float(input('enter the travel speed to destination in kilometer per hours format: '))

travel_time_hours = int(distance // speed)
travel_time_minutes = int(distance % speed)

print(f'you will require {travel_time_hours} hours and {travel_time_minutes} minutes to reach your destination')
