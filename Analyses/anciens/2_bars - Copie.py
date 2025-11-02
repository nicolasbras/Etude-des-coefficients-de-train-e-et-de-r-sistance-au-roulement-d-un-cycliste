import matplotlib.pyplot as plt
import numpy as np
txt_file_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars.txt"

#"C:\Users\nbras\OneDrive\Bureau\donnees_velo_sauvegarde.txt"
##

#données numériques

g=9.8
rho=1.292
Aire=1
m=110


mode_path = r"D:\Ecole\prépa\psi\Mesures_pneus_pression_tipe\2_bars.txt"
f = open(txt_file_path,'r')

LAT=[]
LON=[]
ELE=[]
TEMPS=[]
DT=[]
TEMPS_TOT=[0]

#def remplace(s):
#    return s.replace("<" , ">").encode()


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
del TEMPS[:41]
del TEMPS[:1]#le premier temps apparait 2 fois dans le fichier
LAT=[i*111195 for i in LAT]#conversion des degrés en mètre
LON=[i*111195 for i in LON]
#l'élévation est déjà en mètres


#liste delta-temps et temps accumulé
for i in range(0,len(TEMPS)-1):
    DT.append(abs(float(TEMPS[i+1][17:19])-float(TEMPS[i][17:19])))
    if DT[i]>3: #à corriger, parfois il y a des écarts de 2.0 secondes au passage d'une minute à l'autre.
        DT[i]=1.0
    TEMPS_TOT.append(TEMPS_TOT[i]+DT[i])


#calcul delta-distance
D=[]

for i in range(0,len(LAT)-1):
    d=((LAT[i+1]-LAT[i])**2+(LON[i+1]-LON[i])**2+(ELE[i+1]-ELE[i])**2)**(1/2)
    D.append(d)

#calcul de la vitesse
V=[]
for i in range(0,len(DT)):
    V.append(D[i]/DT[i])


#calcul de la vitesse au carré
V2=[]
for i in range(0,len(DT)):
    V2.append((D[i]/DT[i])**2)


#calcul de l'accélération
ACC=[0]
for i in range(0,len(DT)-1):
    ACC.append(V[i+1]-V[i]/DT[i])


V3=[0]+V#pour que les listes aient les mêmes dimensions

#régression linéaire

P=np.polyfit(V2,ACC,1)
V2NP=np.array(V2)
print("a = ",P[0],"*v² ",P[1])
print("Cr = ",P[1]/(m*g))
print("Cx = ",2*P[0]/(rho*Aire))

#tracés
plt.plot(LAT,LON,'r*')
plt.show()
plt.plot(V2,ACC,'b+')
plt.plot(V2,V2NP*P[0]+P[1],'r-')
plt.show()
plt.plot(TEMPS_TOT,V3,'g+')
plt.show()
f.close()