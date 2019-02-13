#12Feb19
#ping website, get status code


import requests
import schedule
import time


def ping(url):
    r = requests.get(url)
    status = r.status_code
    return status
   


url = 'https://news.ycombinator.com'

status = ping(url)

status_codes = []
status_codes.append(status)

print(status_codes)

