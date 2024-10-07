import numpy as np
from matplotlib import pyplot as plt, patches
import matplotlib.animation as animation
import math
import random
from IPython import display

S = 300 # Numero de Susceptibles iniciales
I = 2 #Numero de Infectados
R = 0 #Numero de recuperados
N = S + I + R  # numero de personas
D = 200  # Tamaño de la ciudad
nc=150 #Numero de casos hasta que empieza a aver tratamiento
pi=np.pi
IR=0.6
l=0.005 #razon de recuperacion
##Tiempo
dt = 0.1
tmin = 0
tmax = 60 * 60  # 100
t = np.arange(tmin, tmax, dt)
##Distancias
lim = D / 50
##Personas
def CirR(CR,n,t):
    r1=D/20 #Desviacionestandar
    pxR=np.array([])
    pyR=np.array([])
    vxR=np.array([])
    vyR=np.array([])
    vx = np.random.uniform(low=-D / 7, high=D / 7, size=N)
    vy = np.random.uniform(low=-D / 7, high=D / 7, size=N)
    vxI = vx[0:I]
    vyI = vy[0:I]
    vx = np.delete(vx, np.arange(0, I))
    vy = np.delete(vy, np.arange(0, I))
    if CR==1:#Rectangulo
        if n==1:
            #Distribucion Normal
            x0 = np.random.uniform(low=0 + lim + r1*2, high=D - r1*2 - lim, size=1)
            y0 = np.random.uniform(low=0 + lim + r1*2, high=D - r1*2 - lim, size=1)
            px = np.random.normal(loc=x0, scale=r1, size=N)  # Scale=sd, loc=mean
            py = np.random.normal(loc=y0, scale=r1, size=N)
        if n!=1:
            #Distribucion Unifomre
            x0 = np.array([])
            y0 = np.array([])
            px = np.random.uniform(low=0 + lim, high=D - lim, size=N)
            py = np.random.uniform(low=0 + lim, high=D - lim, size=N)

    else:#Circular
        if n==1:
            #Distribucion Normal
            angle=np.random.uniform(low=0, high=2*pi, size=1)
            r=np.random.uniform(low=0, high=D/2-r1-lim, size=1)
            x0=r*np.cos(angle) #np.random.uniform(low=0+lim+r1, high=D-r1-lim, size=1)
            y0=r*np.sin(angle)#np.random.uniform(low=0+lim+r1, high=D-r1-lim, size=1)
            px = np.random.normal(loc=x0, scale=r1, size=N)  # Scale=sd, loc=mean
            py = np.random.normal(loc=y0, scale=r1, size=N)
        else:#Uniforme
            x0=np.array([])
            y0=np.array([])
            angle=np.random.uniform(low=0, high=2*pi, size=N)
            r=np.random.uniform(low=0, high=D/2-lim, size=N)
            px=r*np.cos(angle)
            py=r*np.sin(angle)
    pxI = px[0:I]
    pyI = py[0:I]
    px = np.delete(px, np.arange(0, I))
    py = np.delete(py, np.arange(0, I))
    anim(px,py,vx,vy,pxI,pyI,vxI,vyI,pxR,pyR, vxR,vyR,t,CR,x0,y0) ################

# animacion#######################################
def anim(px,py,vx,vy,pxI,pyI,vxI,vyI,pxR,pyR, vxR,vyR,t,CR,x0,y0):

    SS=t*0
    II=t*0
    RR=t*0
    for i in range(len(t)):
        plt.clf()
        #Rectangulo
        if CR==1:
            f1=plt.subplot(1,2,1)
            rectangle = plt.Rectangle((0, 0), D, D, fill=False, ec="red", lw=2)
            plt.gca().add_patch(rectangle)
            plt.axis("off")
            plt.axis('scaled')
        else:
            #Circulo
            f1=plt.subplot(1, 2, 1)
            circle1 = patches.Circle((0, 0), radius=D/2, fill=False, ec="red", lw=3)
            plt.gca().add_patch(circle1)
            plt.axis("off")
            plt.axis('scaled')
        #########################################SIR graficar posiciones###############################################
        plt.plot(px,py,'.',color="blue",label="Susceptibles")#Susceptibles
        S=len(px)
        plt.plot(pxI,pyI, '.', color="red",label=" Infectados")#Infectados
        I=len(pxI)
        plt.plot(pxR,pyR, '.', color="green",label="Recuperados")#Recuperados
        R=len(pxR)
        ###Posicion de punto de prevalencia en la ciudad
        if len(x0)>0:
            plt.plot(x0,y0,"X","Punto de Prevalemcia",color="black")
        plt.legend(loc="upper left")
        #################################################Histograma##################################################
        SS[i]=S
        II[i]=I
        RR[i]=R
        fig=plt.subplot(1,2,2)
        plt.plot(t[0:i],SS[0:i],color="blue",label="Susceptibles")
        plt.plot(t[0:i],II[0:i],color="red",label="Infectados")
        plt.plot(t[0:i], RR[0:i], color="green", label="Recuperados")
        #plt.xlim([t[0], t[-1000]])
        #plt.ylim([0,N])
        plt.legend(loc="upper left")
        ###Euler para movimiento de particulas
        #Posicion x,y de S
        px=px+vx*dt
        py=py+vy*dt
        # Posicion x,y de Infectados
        pxI = pxI+vxI*dt
        pyI= pyI+vyI*dt
        #Posicion x,y de Recuperados
        pxR = pxR + vxR*dt
        pyR = pyR + vyR*dt
        pxR,pyR,pxI,pyI,px,py,vx,vy,vxI,vyI,vxR,vyR =ponh(px, py, pxI, pyI,pxR,pyR,vx,vy,vxI,vyI,vxR,vyR,IR)  ##################################Calculo de distancia
        ###Fronteras
        if CR==1:
            for i in range(0, len(px)):
                if px[i] > D - lim or px[i] < lim:#Limites en Susceptibles
                        vx[i] = -vx[i]
                if py[i] > D - lim or py[i] < lim:
                    vy[i] = -vy[i]
            for j in range(0, len(pxI)):
                if pxI[j] > D - lim or pxI[j] < lim:
                        vxI[j] = -vxI[j]
                if pyI[j] > D - lim or pyI[j] < lim:
                    vyI[j] = -vyI[j]
            for k in range(0, len(pxR)):
                if pxR[k] > D - lim or pxR[k] < lim:
                        vxR[k] = -vxR[k]
                if pyR[k] > D - lim or pyR[k] < lim:
                    vyR[k] = -vyR[k]
        else:
            for i in range(0, len(px)):
                if np.sqrt(px[i]**2+py[i]**2)<0 or np.sqrt(px[i]**2+py[i]**2)>D/2-lim:#Limites en Susceptibles
                    vx[i] = -vx[i]
                    vy[i] = -vy[i]
            for j in range(0, len(pxI)): #Limites de Infectados
                if np.sqrt(pxI[j]**2+pyI[j]**2)<0 or np.sqrt(pxI[j]**2+pyI[j]**2)>D/2-lim:#Limites en Susceptibles
                    vxI[j] = -vxI[j]
                    vyI[j] = -vyI[j]
            for k in range(0, len(pxR)): #Limites de Infectados
                if np.sqrt(pxR[k]**2+pyR[k]**2)<0 or np.sqrt(pxR[k]**2+pyR[k]**2)>D/2-lim:#Limites en Susceptibles
                    vxR[k] = -vxR[k]
                    vyR[k] = -vyR[k]
        plt.pause(0.002)
    plt.axis("off")
    plt.show()

def ponh(px,py,pxI,pyI,pxR,pyR,vx,vy,vxI,vyI,vxR,vyR,IR):
    S=len(px)
    I=len(pxI)
    R=len(pxR)
    #print(S+I+R)
    elim=np.array([])
    NR=int(round((I * l),0))
    if I>=nc:
        if NR!=0:
            NR = int(round((I * l), 0))
        if NR==0:
            NR=1
    elif I>0 and I<nc and S<I:
        if NR!=0:
            NR = int(round((I * l), 0))
        elif NR==0:
            NR=1
    d=random.sample(range(0,I),NR)
    for i in range(0,S):
        for j in range(0,I):
            if np.sqrt((pxI[j] - px[i]) ** 2 + (pyI[j] - py[i]) ** 2) <= IR:
                elim=np.append(elim,i)
    elim=(np.ceil(elim)).astype(int)
    d=(np.ceil(d)).astype(int)
    d=np.sort(d)
    #print(d)
    #agregar
    #print(vxI)
    vxR = np.append(vxR, [vxI[i] for i in d])
    vyR = np.append(vyR, [vyI[i] for i in d])

    pxR = np.append(pxR, [pxI[i] for i in d])
    pyR = np.append(pyR, [pyI[i] for i in d])

    pxI = np.append(pxI, [px[i] for i in elim])
    pyI = np.append(pyI, [py[i] for i in elim])

    vxI=np.append(vxI, [vx[i] for i in elim])
    vyI=np.append(vyI,[vy[i]for i in elim])

    # Restar
    pxI=np.delete(pxI,d)
    pyI=np.delete(pyI,d)
    vxI = np.delete(vxI, d)
    vyI = np.delete(vyI, d)

    vx=np.delete(vx,elim)
    vy=np.delete(vy,elim)
    px=np.delete(px,elim)
    py=np.delete(py,elim)
    return pxR,pyR,pxI,pyI,px,py,vx,vy,vxI,vyI,vxR,vyR

#(1=Rectangulo cualquier otro numero es un circulo ,#1=uniforme cualquier otro numero es distribucion uniforme)
#CirR(1,1,t) #rectangulo con poblacion normal
#CirR(1,2,t) #rectangulo con poblacion uniforme
#CirR(2,1,t) #Circulo con poblacion normal
CirR(2,1,t) #Circulo con poblcacion normal