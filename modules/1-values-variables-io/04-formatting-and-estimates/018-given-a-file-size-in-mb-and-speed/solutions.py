file_size = float(input('enter file size in mb(megabytes): '))
download_speed = float(input('enter your download speed in mb/s(mbps): '))

download_time = file_size / download_speed

total_time_in_minutes = download_time // 60
total_time_in_seconds = download_time % 60

print(f'you will require {int(total_time_in_minutes)} minutes and {total_time_in_seconds:.2f} seconds to complete the download')