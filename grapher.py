#14Feb19 
#Pull from csv, plot using plt

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):


headers = ['status', 'DTG']
data = pd.read_csv('status_codes.csv', names=headers)
print(data)

x = data['DTG']
y = data['status']

#plot
while True:
    time.sleep(5)
    plt.scatter(x, y, s = 100)
    plt.axis([0, 500,:
    plt.show()
    plt.pause(0.0001)
    
