import matplotlib.pyplot as plt
import scipy.special as special
import numpy as np
from scipy import integrate
txt_file_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars.txt"

#"C:\Users\nbras\OneDrive\Bureau\donnees_velo_sauvegarde.txt"
##

#données numériques

g=9.8 #accélération de la pesanteur en m/s-2
rho=1.225 #masse volumique de l'air en kg/m3
Aire=0.5 #aire projetée totale en m²
m=65+15.5 #masse totale en kg


mode_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars.txt"
f = open(txt_file_path,'r')

LAT=[]
LON=[]
ELE=[]
TEMPS=[]
DT=[]
TEMPS_TOT=[0]
lat_balise="lat=_" #il faut remplacer dans le fichier les " par des _
ele_balise=">ele>" #il faut remplacer dans le fichier les < par des >
temps_balise=">time>"
balise1="_"
balise2=">" #il faut remplacer dans le fichier les Z par des >

#liste latitude et longitude
with open(txt_file_path) as f:
    for line in f:
        pos_begin=line.find(lat_balise)
        if pos_begin!=-1:
            A=line.split(balise1)
            LAT.append(float(A[1]))
            LON.append(float(A[3]))
#liste élévation
with open(txt_file_path) as f:
    for line in f:
        pos_begin=line.find(ele_balise)
        if pos_begin!=-1:
            A=line.split(balise2)
            ELE.append(float(A[2]))
#liste temps
with open(txt_file_path) as f:
    for line in f:
        pos_begin=line.find(temps_balise)
        if pos_begin!=-1:
            A=line.split(balise2)
            TEMPS.append(A[2])


del LAT[:32]
del LON[:32]
del ELE[:32]
del TEMPS[:33]#le premier temps apparait 2 fois dans le fichier

del LAT[-8:]
del LON[-8:]
del ELE[-8:]
del TEMPS[-8:]

R=6371.009*10**3 #rayon de la Terre
LAT=[i*R*np.pi/180 for i in LAT]#conversion des degrés en mètre
LON=[i*R*np.pi/180 for i in LON]
#l'élévation est déjà en mètres

#liste delta-temps et temps accumulé
for i in range(0,len(TEMPS)-1):
    DT.append(abs(float(TEMPS[i+1][17:19])-float(TEMPS[i][17:19])))
#    if DT[i]>3: #à corriger, parfois il y a des écarts de 2.0 secondes au passage d'une minute à l'autre.
#        DT[i]=1.0
    TEMPS_TOT.append(TEMPS_TOT[i]+DT[i])

print(LAT[0:10])
#calcul delta-distance
D=[]
DTOT=[0]

for i in range(0,len(LAT)-1):
    d=np.sqrt((LAT[i+1]-LAT[i])**2+(LON[i+1]-LON[i])**2+(ELE[i+1]-ELE[i])**2)
    D.append(d)#On multiplie par 1,875 car cela correspond mieux à la réalité mesurée par Strava (la distance totale mesurée est de 150m)
    DTOT.append(DTOT[i]+D[i])

#régression linéaire

L=np.polyfit(TEMPS_TOT,DTOT,4)
t=np.linspace(0,TEMPS_TOT[-1],len(TEMPS_TOT))


def position(t):
    return L[0]*t**4+L[1]*t**3+L[2]*t**2+L[3]*t+L[4]

plt.plot(t,DTOT,'b--')
plt.plot(t,position(t),'r+')
plt.show()

def vitesse(t):
    return (4*L[0]*t**3+3*L[1]*t**2+2*L[2]*t+L[3])#0.32

plt.plot(t,vitesse(t),'b+')
plt.show()

def acceleration(t):
    return (12*L[0]*t**2+6*L[1]*t+2*L[2])

plt.plot(t,acceleration(t),'b+')
plt.show()

VQ=[]
ACC=[]

for i in range(0,len(t)):
    VQ.append(vitesse(t[i])**2)
    ACC.append(acceleration(t[i]))

#On supprime les 6 dernières valeurs qui sont aberantes
#del VQ[-6:]
#del ACC[-6:]

VQ=np.array(VQ)
ACC=np.array(ACC)

P=np.polyfit(VQ,ACC,1)
print("a = ",P[0],"*v² ",P[1])
print("Cr = ",abs(P[1]/(m*g)))
print("Cx = ",abs(2*P[0]/(rho*Aire)))
print(len(TEMPS_TOT),len(DTOT))

plt.plot(VQ,ACC,'b+')
plt.plot(VQ,P[0]*VQ+P[1])
plt.show()
plt.close()

##Nouvelle conversion (pas au point)
R=6371.009*10**3 #rayon de la Terre en m
for i in range(0,len(LAT)):
    LAT[i]=R*np.cos(LAT[i]*np.pi/180)*np.cos(LON[i]*np.pi/180)
    LON[i]=R*np.cos(LAT[i]*np.pi/180)*np.sin(LON[i]*np.pi/180)