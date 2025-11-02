import matplotlib.pyplot as plt
import scipy.special as special
import numpy as np
txt_file_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars.txt"

#"C:\Users\nbras\OneDrive\Bureau\donnees_velo_sauvegarde.txt"
##

#données numériques

g=9.81 #accélération de la pesanteur en m/s-2
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


del LAT[:40]
del LON[:40]
del ELE[:40]
del TEMPS[:40]#le premier temps apparait 2 fois dans le fichier

del LAT[-4:]
del LON[-4:]
del ELE[-4:]
del TEMPS[-4:]

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
TEMPS_TOT.pop(0)

#calcul delta-distance
D=[]
DTOT=[0]

for i in range(0,len(LAT)-1):
    d=np.sqrt((LAT[i+1]-LAT[i])**2+(LON[i+1]-LON[i])**2+(ELE[i+1]-ELE[i])**2)
    D.append(d)
    DTOT.append(DTOT[i]+D[i])

#régression linéaire

L=np.polyfit(TEMPS_TOT,DTOT,4)
t=np.linspace(0,TEMPS_TOT[-1],len(TEMPS_TOT))


def position(t):
    return L[0]*t**4+L[1]*t**3+L[2]*t**2+L[3]*t+L[4]

plt.plot(t,position(t),'b+')
plt.title("Distance parcourue en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xlabel("temps en s",size=20,)
plt.ylabel("Distance en m", size=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()

def vitesse(t):
    return (4*L[0]*t**3+3*L[1]*t**2+2*L[2]*t+L[3])

plt.plot(t,vitesse(t),'b+')
plt.title("Vitesse en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22},)
plt.xlabel("temps en s",size=20,)
plt.ylabel("Vitesse en m/s", size=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()

def acceleration(t):
    return (12*L[0]*t**2+6*L[1]*t+2*L[2])

plt.plot(t,acceleration(t),'b+')
plt.xlabel("temps en s",size=20)
plt.ylabel("accélération en m/s²",size=20)
plt.title("Accélération en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()

VQ=[]
ACC=[]

for i in range(0,len(t)):
    VQ.append(vitesse(t[i])**2)
    ACC.append(acceleration(t[i]))

#On supprime les 6 dernières valeurs qui sont aberantes
del VQ[-6:]
del ACC[-6:]

VQ=np.array(VQ)
ACC=np.array(ACC)

P=np.polyfit(VQ,ACC,1)
print("Cr = ",round(abs(P[1]/g),4))

plt.plot(VQ,ACC,'b+')
plt.plot(VQ,P[0]*VQ+P[1])
plt.xlabel("vitesse au carré",size=20)
plt.ylabel("accélération en m/s²",size=20)
plt.title("accélération en fonction de la vitesse au carré",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
plt.show()
plt.close()

