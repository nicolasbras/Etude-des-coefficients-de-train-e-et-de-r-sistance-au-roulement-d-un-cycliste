import matplotlib.pyplot as plt
import scipy.special as special
import numpy as np
txt_file_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\mesures 4\40 psi\6.gpx"

#"C:\Users\nbras\OneDrive\Bureau\donnees_velo_sauvegarde.txt"
##

#données numériques

g=9.81 #accélération de la pesanteur en m/s-2
rho=1.225 #masse volumique de l'air en kg/m3
Aire=0.5 #aire projetée totale en m²
m=65+15.5 #masse totale en kg


mode_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\mesures 4\40 psi\6.gpx"
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


#del LAT[:9]
#del LON[:9]
#del ELE[:9]
#del TEMPS[:9]

#del LAT[-3:]
#del LON[-3:]
#del ELE[-3:]
#del TEMPS[-3:]

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

print(DTOT)
print(TEMPS_TOT)
plt.plot(TEMPS_TOT,DTOT,'r+')
plt.show()