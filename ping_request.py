#12Feb19
#ping website, get status code


import requests

def ping(url):
    #   Ping url and get status code, return code
    r = requests.get(url)
    status = r.status_code
    return status
   
#set url to ping, print status code


