# uptime_tracker
Python uptime tracker page

This app will ping a healthcheck endpoint with scheduler.py, append result/time to status_codes.csv, and then using 
pygal or matplotlib or similar, produce an uptime chart. 

Runs in background, currently every 5 seconds
