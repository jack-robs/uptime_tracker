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
    x = data['DTG']
    y = data['status']
    ax1.clear()
    ax1.plot(x, y)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


