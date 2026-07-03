minutes = float(input('enter total time in minutes: '))

hours = int(minutes / 60)
rem_minutes = int(minutes % 60)

print(f'total hours: {hours} total minutes: {rem_minutes}')