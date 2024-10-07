
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
D=200
N=5
dt=10
# create empty lists for the x and y data
x = []
y = []
#px=np.random.uniform(low=0, high=D-5, size=N)
#py=np.random.uniform(low=0, high=D-5, size=N)
#vx=np.random.uniform(low=-D/100, high=D/100, size=N)
#vy=np.random.uniform(low=-D/100, high=D/100, size=N)
# create the figure and axes objects
fig, ax = plt.subplots()
def animate(i):
    # grab a random integer to be the next y-value in the animation
    px=px+vx*dt
    py=py+vy*dt
    ax.clear()
    ax.plot(px, py)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])

ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)
plt.show()