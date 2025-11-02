import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
txt_file_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars_B.txt"

#"C:\Users\nbras\OneDrive\Bureau\donnees_velo_sauvegarde.txt"
##

#données numériques

g=9.8 #accélération de la pesanteur en m/s-2
rho=1.225 #masse volumique de l'air en kg/m3
Aire=0.5 #aire projetée totale en m²
m=65+15.5 #masse totale en kg


mode_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars_B.txt"
f = open(txt_file_path,'r')

#Initialisation des listes

LAT=[]
LON=[]
ELE=[]
TEMPS=[]
DT=[]
TEMPS_TOT=[0]

#Paramétrage des balises

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

#Suppression des valeurs en dehors de la décélération

#del LAT[:43]
#del LON[:43]
#del ELE[:43]
#del TEMPS[:44]#le premier temps apparait 2 fois dans le fichier
TEMPS.pop(0)

R=6371.009*10**3 #rayon de la Terre
LAT=[i*R*np.pi/180 for i in LAT]#conversion des degrés en mètre
LON=[i*R*np.pi/180 for i in LON]
#l'élévation est déjà en mètres

#liste delta-temps et temps accumulé
for j in range(0,len(TEMPS)-1):
    if (float(TEMPS[j+1][17:19])<float(TEMPS[j][17:19])):
        DT.append(abs(float(TEMPS[j+1][17:19])-float(TEMPS[j][17:19])+60))
    else:
        DT.append(abs(float(TEMPS[j+1][17:19])-float(TEMPS[j][17:19])))
    TEMPS_TOT.append(TEMPS_TOT[j]+DT[j])

#calcul delta-distance
D=[]
DTOT=[0]

for i in range(0,len(LAT)-1):
    d=np.sqrt((LAT[i+1]-LAT[i])**2+(LON[i+1]-LON[i])**2+(ELE[i+1]-ELE[i])**2)
    D.append(d)
    DTOT.append(DTOT[i]+D[i])

#Dérivation discrète

V=[]
A = []

t1=np.linspace(TEMPS_TOT[0],TEMPS_TOT[-1],len(TEMPS_TOT))

for i in range(1,len(DTOT)-1):
    V.append((DTOT[i+1]-DTOT[i-1])/(t1[i+1]-t1[i-1]))

TEMPS_TOT.pop(0)
TEMPS_TOT.pop(-1)

t2=np.linspace(TEMPS_TOT[0],TEMPS_TOT[-1],len(TEMPS_TOT))

for i in range(1,len(V)-1):
    A.append((V[i+1]-V[i-1])/(t2[i+1]-t2[i-1]))

TEMPS_TOT.pop(0)
TEMPS_TOT.pop(-1)

t3=np.linspace(TEMPS_TOT[0],TEMPS_TOT[-1],len(TEMPS_TOT))


plt.plot(t1,DTOT,'b--')
plt.show()

plt.plot(t2,V,'b+')
plt.show()

plt.plot(t3,A,'b+')
plt.show()

#On supprime les 6 dernières valeurs qui sont aberantes
#del V[-6:]
#del A[-6:]
#del V[:1]
#del A[:1]

#On supprime les bords de V pour qu'il ait le même nombre d'éléments que A
V.pop(0)
V.pop(-1)

V=np.array(V)
V=np.square(V)
A=np.array(A)



P=np.polyfit(V,m*A,1)
print("m*a = ",P[0],"*v² ",P[1])
print("Cr = ",abs(P[1]/(m*g)))
print("Cx = ",abs(2*P[0]/(rho*Aire)))
print(len(TEMPS_TOT),len(DTOT))

plt.plot(V,m*A,'b+')
plt.plot(V,P[0]*V+P[1])
plt.show()
plt.close()