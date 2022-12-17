import pytz
from datetime import datetime

naive_time = datetime(2018, 3, 31, 12, 0, 0)
utc_time = pytz.utc.localize(naive_time)
ny_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

print(utc_time.strftime('%s'))
print(ny_time.strftime('%s'))

epoch_start = pytz.utc.localize(datetime(1970, 1, 1))
print((utc_time - epoch_start).total_seconds())
print((ny_time - epoch_start).total_seconds())

print(utc_time.timestamp())
print(ny_time.timestamp())
