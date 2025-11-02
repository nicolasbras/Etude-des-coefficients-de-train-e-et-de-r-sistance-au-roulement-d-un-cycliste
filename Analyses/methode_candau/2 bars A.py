import matplotlib.pyplot as plt
import scipy.special as special
import numpy as np
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

#liste delta-temps et temps accumulé
for i in range(0,len(TEMPS)-1):
    DT.append(abs(float(TEMPS[i+1][17:19])-float(TEMPS[i][17:19])))
#    if DT[i]>3: #à corriger, parfois il y a des écarts de 2.0 secondes au passage d'une minute à l'autre.
#        DT[i]=1.0
    TEMPS_TOT.append(TEMPS_TOT[i]+DT[i])

R=6371.009*10**3 #rayon de la Terre
LAT=[i*R*np.pi/180 for i in LAT]#conversion des degrés en mètre
LON=[i*R*np.pi/180 for i in LON]
#l'élévation est déjà en mètres

t11,t12,t21,t22=TEMPS_TOT[40],TEMPS_TOT[41],TEMPS_TOT[50],TEMPS_TOT[51]

d1,d2=np.sqrt((LAT[40+1]-LAT[40])**2+(LON[40+1]-LON[40])**2+(ELE[40+1]-ELE[40])**2),np.sqrt((LAT[50+1]-LAT[50])**2+(LON[50+1]-LON[50])**2+(ELE[50+1]-ELE[50])**2)

v1,v2=d1/(t12-t11),d2/(t22-t21)

dt=(t21+t22-t11-t12)/2

a=(v2-v1)/dt

vmoy=(v1+v2)/2

print("m*a = ",m*a)
print("vmoy² = ",vmoy*vmoy)