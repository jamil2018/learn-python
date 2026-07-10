seconds = int(input('enter time in seconds: '))

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR 

total_days = int(seconds / DAY)
total_hours = int((seconds % DAY) / HOUR)
total_minutes = int((seconds % DAY) % HOUR / MINUTE)
total_seconds = ((seconds % DAY) % HOUR) % MINUTE


print(f'{total_days} day(s) {total_hours} hour(s) {total_minutes} minute(s) {total_seconds} second(s)')
