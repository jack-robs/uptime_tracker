#12Feb19
#ping website, get status code


import requests
import datetime
import csv 


url = 'https://news.ycombinator.com'
filename = 'status_codes.csv'


def ping(url):
    #   Ping url and get status code, return code
    r = requests.get(url)
    status = r.status_code
    return status
   
#set url to ping, print status code

status = ping(url)
now = datetime.datetime.now()
time = now.isoformat()

with open(filename, 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([status,time])

print(status, time)




#write to csv

