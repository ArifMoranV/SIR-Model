import numpy as np
from matplotlib import pyplot as plt, patches
# import matplotlib.animation as animation
import math
from IPython import display

S = 100
I = 5
R = 0
N = S + I + R  # numero de personas
IR = 5  # Radio de infeccion
RR = 0.06  # razon de recuperacion
lim = 4  #
D = 200  # Tamaño de la ciudad

#def Recuperados():

def graph(px,py,pxI,pyI):
    plt.plot(pxI, pyI, '.', color='red', markersize=5, label="Infectados")
    plt.plot(px, py, '.', color='blue', markersize=1, label="Susceptibles")
    plt.axis('scaled')
    plt.axis('off')
    plt.legend(loc="upper left")
    plt.close()

    
###Funcionde calculos de distancia
def distancia(px, py, pxI, pyI,S,I,IR):
    elim=np.array([])
    for i in range(S):
        for j in range(I):
            if math.sqrt((pxI[j] - px[i]) ** 2 + (pyI[j] - py[i]) ** 2) <= IR:
                elim=np.append(elim,i)
    elim=(np.ceil(elim)).astype(int)
    pxI = np.append(pxI, [px[i] for i in elim])
    pyI = np.append(pyI, [py[i] for i in elim])
    px=np.delete(px,elim)
    py=np.delete(py,elim)
    return pxI, pyI,px,py,len(px),len(pxI)

#Ciudad cuadrada#############################################
#Posiciones
px = np.random.uniform(low=0 + lim, high=D - lim, size=N)
py = np.random.uniform(low=0 + lim, high=D - lim, size=N)
vx = np.random.uniform(low=-D / 7, high=D / 7, size=N)
vy = np.random.uniform(low=-D / 7, high=D / 7, size=N)
#Plot de la ciudad rectangular
fig, ax = plt.subplots()
rectangle = plt.Rectangle((0, 0), D, D, fill=False, ec="red", lw=2)
plt.gca().add_patch(rectangle)
#Clasificacion de infectados y Susceptibles
pxI = px[0:I]
pyI = py[0:I]
px = np.delete(px, np.arange(0,I))
py = np.delete(py, np.arange(0,I))
###grafica de personas
Inf = plt.plot(pxI, pyI, '.', color='red', markersize=5, label="Infectados")
Sus = plt.plot(px, py, '.', color='blue', markersize=1, label="Susceptibles")
plt.axis('scaled')
plt.axis('off')
plt.legend(loc="upper left")
plt.close()

# Ciudad circular#######################################################################
fig2 = plt.figure()
ax = fig2.add_subplot()
circle1 = patches.Circle((0, 0), radius=D / 2, fill=False, ec="red", lw=3)
ax.add_patch(circle1)
ax.axis('equal')
pi = math.pi
xx = np.random.uniform(low=0, high=(2 * pi), size=N)
r = np.random.uniform(low=0, high=(D / 2) - lim, size=N)
##Clasificar
px = r * np.cos(xx)
py = r * np.sin(xx)
pxI = px[0:I]
pyI = py[0:I]
px = np.delete(px, np.arange(0,I))
py = np.delete(py, np.arange(0,I))
Inf = plt.plot(pxI, pyI, '.', color='red', markersize=5, label="Infectados")
Sus = plt.plot(px, py, '.', color='blue', markersize=1, label="Susceptibles")
plt.axis('off')
plt.legend(loc="upper left")
plt.close()

# Cluster en ciudad cuadrada ###########################################################################3
fig, ax = plt.subplots()
rectangle = plt.Rectangle((0, 0), D, D, fill=False, ec="red", lw=2)
plt.gca().add_patch(rectangle)
plt.axis('scaled')
##Lugar preferencial(Cluster)
r1 = D / 20
v = np.random.uniform(low=0 + lim + r1, high=D - lim - r1, size=2)
x0 = v[0]
y0 = v[1]
px = np.random.normal(loc=x0, scale=r1, size=N)  # Scale=sd, loc=mean
py = np.random.normal(loc=y0, scale=r1, size=N)
# Resto de la Ciudad##########################
plt.plot(x0, y0, "X", color="black", label="Punto preferencial")
#Clasificar Inf y susc
pxI = px[0:I]
pyI = py[0:I]
px = np.delete(px, np.arange(0,I))
py = np.delete(py, np.arange(0,I))

#Chequeo de Infeccion
pxI, pyI, px, py,S,I= distancia(px, py,pxI, pyI,S,I,IR)  ################################################################################
plt.plot(pxI, pyI, '.', color='red', markersize=5, label="Infectados")
plt.plot(px, py, '.', color='blue', markersize=1, label="Susceptibles")
plt.axis("off")
plt.legend(loc="upper center")
plt.show()

# Cluster en ciudad circular #################
fig2 = plt.figure()
ax = fig2.add_subplot()
circle1 = patches.Circle((0, 0), radius=D / 2, fill=False, ec="red", lw=3)
ax.add_patch(circle1)
# Punto preferencial de la ciudad
r1 = D / 20
v = np.random.uniform(low=0, high=2 * pi, size=1)
r = np.random.uniform(low=0, high=D / 2 - r1, size=1)
x0 = r[0] * np.cos(v[0])
y0 = r[0] * np.sin(v[0])
##Cluster
px = np.random.normal(loc=x0, scale=r1, size=N)  # Scale=sd, loc=mean
py = np.random.normal(loc=y0, scale=r1, size=N)
#Infectados y Susceptibles
pxI = px[0:I]
pyI = py[0:I]
px = np.delete(px, np.arange(0,I))
py = np.delete(py, np.arange(0,I))
###Plots
plt.plot(x0, y0, "X", color="black", label="Punto preferencial")
plt.plot(pxI,pyI, '.', color='red', markersize=5, label="Infectados")
plt.plot(px, py, '.', color='blue', markersize=1, label="Susceptibles")
ax.axis('equal')
plt.axis("off")
plt.legend(loc="upper center")
plt.show()
