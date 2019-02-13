#scheduler for ping function

from ping_request import ping
import datetime
import csv 
import time

url = 'https://news.ycombinator.com'
filename = 'status_codes.csv'


status = ping(url)
now = datetime.datetime.now()
time = now.isoformat()

with open(filename, 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([status,time])

print(status, time)


