import numpy as np
from matplotlib import pyplot as plt,patches
import matplotlib.animation as animation
import math
from IPython import display

S=5
I=1
R=0
N=S+I+R #numero de personas

D=200 # Tamaño de la ciudad
#x=np.linspace(0,D,100)
#y=np.linspace(0,D,100)

#fig=plt.figure()
#Ciudad

fig,ax= plt.subplots()
rectangle = plt.Rectangle((0,0),D, D,fill=False,ec="red",lw=2)
plt.gca().add_patch(rectangle)
plt.axis('scaled')

##Personas
px=np.random.uniform(low=0, high=D-5, size=N)
py=np.random.uniform(low=0, high=D-5, size=N)
vx=np.random.uniform(low=-D/1000, high=D/1000, size=N)
vy=np.random.uniform(low=-D/1000, high=D/1000, size=N)
dt=0.1
tmin=0
tmax=10 #100
t=np.arange(tmin,tmax+1,dt)

pxn=px
px1=px
py1=py
pyn=py
for i in range(0,len(t)):
    pxn=(px1+vx*t[i])
    pyn=(py1+vy*t[i])
    px=[px,pxn]
    py=[py,pyn]
    #px=pxn
    #py=pyn
    for k in range(0,len(px)):
        if (pxn[k]<5 or pxn[k]>D-5):
            vx[k]=-vx[k]
        if pyn[k]<5 or pyn[k]>D-5:
            vy[k]=-vy[k]

#px=np.asmatrix(px)
#py=np.asmatrix(py)
    

#animacion####################################33

pos, = ax.plot([],[],'.')
def animate(frame):
    pos.set_data((px[frame],py[frame]))
    return pos,

Ani=animation.FuncAnimation(fig,animate,frames=np.linspace(0,len(t)),interval=2000,repeat=True)
plt.axis("off")
plt.show()