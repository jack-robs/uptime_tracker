#scheduler for ping function

from ping_request import ping
import datetime
import csv 
import time

url = 'https://news.ycombinator.com'
filename = 'status_codes.csv'

while True:
    time.sleep(5)
    status = ping(url)
    now = datetime.datetime.now()
    current_time = now.isoformat()

    with open(filename, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([status, current_time])
        

#    print(status, current_time)


