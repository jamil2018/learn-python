progress_percentage = int(input('enter progress percentage: '))

remainder = 100 - progress_percentage
print(f'progress: [{"*"*progress_percentage}{" ":>{remainder}}]')