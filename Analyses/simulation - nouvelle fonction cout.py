##Remarques sur la fonction cout
#La liste créée par Odeint est plus longue et n'est donc pas indicée comme la liste originale DTOT. Cette dernière est telle que DTOT[i] est la distance parcourue à l'instant t=i secondes. On ne peut donc pas comparer les valeurs car on ne connait pas l'indice de la liste de Odeint pour laquelle t=i.
#Idée : on pourrait faire le calcul des aires entre les courbes




##Remarques
#Le premier passage s'est produit à une vitesse trop élevée. On n'observe aucune décélération, dû au fait que le vélo est toujours influencé par l'effet d'inertie qui le propulse.
#Cr2 = 0.021
#Cr3 = 0.018
#Cr4 = 0.027
#Cr5 = 0.015

##Données
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
from scipy.interpolate import interp1d
from scipy.integrate import odeint
from ipywidgets import interact

#Données
M=84 #masse du vélo+cycliste
g=9.8
Cx=0.8 #coefficient de trainée
rho=1.212 #masse volumique de l'air
S=0.5 #surface frontale
Cr=0.004 #coefficient de roulement
theta=0*np.pi/180 #angle de la pente
##Mesures
DTOT40psi1=[8.17771470773408, 17.637142632121083, 28.02410197888254, 38.97656867823143, 49.363046641202715, 59.00232569537784, 68.14469865424132, 77.0471195408489, 85.87645731842237, 94.56805059317196, 103.19911011877284, 110.65565774538418, 117.80421317152441, 124.84822645132465]

TEMPS_TOT40psi1=[10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0]

DTOT40psi2=[43.02146375768431, 54.754420383768775, 66.38108808658114, 77.04295652974012, 86.82053947501377, 96.8778927826605, 106.0922079530244, 114.35737674796712, 121.95356272786715, 127.83935366516205]

TEMPS_TOT40psi2=[5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]

DTOT40psi3=[85.01504041180081, 92.68347132322445, 100.56563330716587, 107.32021983163071, 113.84671768206046, 120.18660148173849, 126.34263287093934, 132.04164807451212, 137.57129808585276, 141.3747551414146]

TEMPS_TOT40psi3=[35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0]

DTOT40psi4=[60.16383557363731, 71.9451678870685, 83.24217730199341, 93.83609888404895, 103.19024859730455, 112.89548392337255, 121.69382524416669, 130.20501450547061, 138.11863666958678, 145.6813810937239, 150.7633842220559]

TEMPS_TOT40psi4=[6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]

DTOT40psi5=[0, 8.193048146487737, 16.41983787224445, 23.9195320582378, 31.390319215738646, 38.66982643565665, 45.28383115523552, 51.40946807874154, 57.64135485663523, 63.84440626351948, 70.15594811503108, 75.30705361762745, 80.30217639171786, 84.80797900520017, 89.20800201600761, 93.32222011373835, 97.25198715025826, 101.18302632050377, 104.22009770488258, 107.30363180949112, 110.3646464143657, 113.03795753683696, 115.95669610641956]

TEMPS_TOT40psi5=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0]
##Fonction 40 psi 1
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT40psi1"
TI=TEMPS_TOT40psi1[0]
TF=TEMPS_TOT40psi1[-1]
N=100
T=(TF-TI)/N
x0=DTOT40psi1[0]
v0=(DTOT40psi1[1]-DTOT40psi1[0])/(TEMPS_TOT40psi1[1]-TEMPS_TOT40psi1[0])

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(TI,TF,N)
    X = np.zeros(N+1)
    V = np.zeros(N+1)
    X[0]=x0
    V[0]=v0
    for i in range(N):
        Vect=np.array([X[i],V[i]])
        D=F(Vect,temps[i])
        V[i+1]=V[i]+D[1]*T
        X[i+1]=X[i]+D[0]*T
    return X,V

X,V=euler(F,x0,v0,T,N)
t=np.linspace(TI,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,4):
    #Cx+=i/100
    Cr+=j/100
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT40psi1,DTOT40psi1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.04
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.02
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]

        CR={"Cr1":Cr,"Cr2":Cr+app,"Cr3":Cr-app}
        COUT={"cout1":0,"cout2":0,"cout3":0}


        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        T=np.linspace(0,TF,len(X1))

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi1)):
            COUT["cout1"]+=abs(DTOT40psi1[j]-f(TEMPS_TOT40psi1[j]))

        Cr=CR["Cr2"]

        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi1)):
            COUT["cout2"]+=abs(DTOT40psi1[j]-f(TEMPS_TOT40psi1[j]))

        Cr=CR["Cr3"]

        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi1)):
            COUT["cout3"]+=abs(DTOT40psi1[j]-f(TEMPS_TOT40psi1[j]))

        print(COUT)
        print(CR)


        minimum=min(COUT,key=COUT.get)
        Cr=CR["Cr"+minimum[-1]]

        print(CR["Cr"+minimum[-1]])

        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres : ',round(min(COUT.values()),3))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi1,DTOT40psi1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonction 40 psi 2
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT40psi2"
TI=TEMPS_TOT40psi2[0]
TF=TEMPS_TOT40psi2[-1]
N=100
T=(TF-TI)/N
x0=DTOT40psi2[0]
v0=(DTOT40psi2[1]-DTOT40psi2[0])/(TEMPS_TOT40psi2[1]-TEMPS_TOT40psi2[0])

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(TI,TF,N)
    X = np.zeros(N+1)
    V = np.zeros(N+1)
    X[0]=x0
    V[0]=v0
    for i in range(N):
        Vect=np.array([X[i],V[i]])
        D=F(Vect,temps[i])
        V[i+1]=V[i]+D[1]*T
        X[i+1]=X[i]+D[0]*T
    return X,V

X,V=euler(F,x0,v0,T,N)
t=np.linspace(TI,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,4):
    #Cx+=i/100
    Cr+=j/100
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT40psi2,DTOT40psi2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.018
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.018
    Cx=3
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]

        CX={"Cx1":Cx,"Cx2":Cx+app,"Cx3":Cx-app}
        COUT={"cout1":0,"cout2":0,"cout3":0}


        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        T=np.linspace(0,TF,len(X1))

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi2)):
            COUT["cout1"]+=np.sqrt((DTOT40psi2[j]-f(TEMPS_TOT40psi2[j]))**2)
            print(DTOT40psi2[j])
            print(f(TEMPS_TOT40psi2[j]))

        Cx=CX["Cx2"]

        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi2)):
            COUT["cout2"]+=np.sqrt((DTOT40psi2[j]-f(TEMPS_TOT40psi2[j]))**2)

        Cx=CX["Cx3"]

        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])

        f=interp1d(T,X1,kind='linear')

        for j in range(0,len(TEMPS_TOT40psi2)):
            COUT["cout3"]+=np.sqrt((DTOT40psi2[j]-f(TEMPS_TOT40psi2[j]))**2)

        print(COUT)
        print(CX)


        minimum=min(COUT,key=COUT.get)
        Cx=CX["Cx"+minimum[-1]]

        print(CX["Cx"+minimum[-1]])

        print(m,"Cx = ",round(Cx,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres : ',round(min(COUT.values()),3))
    return round(Cx,6)

dichotomie(50,1/10,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi2,DTOT40psi2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonction 40 psi 3
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT40psi3"
TI=TEMPS_TOT40psi3[0]
TF=TEMPS_TOT40psi3[-1]
N=100
T=(TF-TI)/N
x0=DTOT40psi3[0]
v0=(DTOT40psi3[1]-DTOT40psi3[0])/(TEMPS_TOT40psi3[1]-TEMPS_TOT40psi3[0])

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(TI,TF,N)
    X = np.zeros(N+1)
    V = np.zeros(N+1)
    X[0]=x0
    V[0]=v0
    for i in range(N):
        Vect=np.array([X[i],V[i]])
        D=F(Vect,temps[i])
        V[i+1]=V[i]+D[1]*T
        X[i+1]=X[i]+D[0]*T
    return X,V

X,V=euler(F,x0,v0,T,N)
t=np.linspace(TI,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,4):
    #Cx+=i/100
    Cr+=j/100
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT40psi3,DTOT40psi3,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.04
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.01
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT40psi3[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT40psi3[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi3,DTOT40psi3,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonction 40 psi 4
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT40psi4"
TI=TEMPS_TOT40psi4[0]
TF=TEMPS_TOT40psi4[-1]
N=100
T=(TF-TI)/N
x0=DTOT40psi4[0]
v0=(DTOT40psi4[1]-DTOT40psi4[0])/(TEMPS_TOT40psi4[1]-TEMPS_TOT40psi4[0])

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(TI,TF,N)
    X = np.zeros(N+1)
    V = np.zeros(N+1)
    X[0]=x0
    V[0]=v0
    for i in range(N):
        Vect=np.array([X[i],V[i]])
        D=F(Vect,temps[i])
        V[i+1]=V[i]+D[1]*T
        X[i+1]=X[i]+D[0]*T
    return X,V

X,V=euler(F,x0,v0,T,N)
t=np.linspace(TI,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,4):
    #Cx+=i/100
    Cr+=j/100
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT40psi4,DTOT40psi4,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.04
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.01
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT40psi4[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT40psi4[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi4,DTOT40psi4,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonction 40 psi 5
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT40psi5"
TI=TEMPS_TOT40psi5[0]
TF=TEMPS_TOT40psi5[-1]
N=100
T=(TF-TI)/N
x0=DTOT40psi5[0]
v0=(DTOT40psi5[1]-DTOT40psi5[0])/(TEMPS_TOT40psi5[1]-TEMPS_TOT40psi5[0])

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(TI,TF,N)
    X = np.zeros(N+1)
    V = np.zeros(N+1)
    X[0]=x0
    V[0]=v0
    for i in range(N):
        Vect=np.array([X[i],V[i]])
        D=F(Vect,temps[i])
        V[i+1]=V[i]+D[1]*T
        X[i+1]=X[i]+D[0]*T
    return X,V

X,V=euler(F,x0,v0,T,N)
t=np.linspace(TI,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,4):
    #Cx+=i/100
    Cr+=j/100
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT40psi5,DTOT40psi5,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.04
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.01
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT40psi5[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT40psi5[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi5,DTOT40psi5,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()