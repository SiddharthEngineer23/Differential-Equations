import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import pandas as pd
import numpy as np
import time
import math

#creating our animation variables
fig, ax = plt.subplots()
ax.set_xlim(0,10000)
ax.set_ylim(0,25000)
line, = ax.plot(0,0)
plt.title(label="Forwards Real Word: wabbits; Step=80")

# #putting x and y axes
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# x = np.array([1.571, 3.142, 4.712, 6.283, 7.854, 9.425, 11.001, 12.566])
# my_xticks = ['\u03C0/2', '\u03C0', '3\u03C0/2', '2\u03C0', '5\u03C0/2', '3\u03C0', '7\u03C0/2', '4\u03C0']
# plt.xticks(x, my_xticks)

# #plotting our regular quadratic to compare
# x = np.arange(-1,15,0.1)
# y = []

# for item in x:
#     val = math.cos(item)
#     y.append(val)
# #y = x**2
# plt.plot(x, y)

#storing points of x and y
x_data = [0]
y_data = [2000]
step = 80

def animation_frame(i):

    #getting last x and y value
    val_x = x_data[len(x_data) - 1]
    val_y = y_data[len(y_data) - 1]

    #updating data (for some reason it passes i=0 in twice)
    x_data.append(i)
    if(i == 0):
        y_data.append(2000)
    else:
        #y_data.append((step*(-val_y)) + val_y)
        y_data.append(val_y + step * ((val_y/900)*(1-(val_y/20000))))

    #updating plot
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    #print(str(i) + " : " + str(val_x) + " : " + str(val_y))

    return line,

#animation functions
# animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,10000,step), interval=1)
# plt.show()

writer = PillowWriter(fps=500)
animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0,10000,step))
animation.save("real_world.gif", writer=writer)
