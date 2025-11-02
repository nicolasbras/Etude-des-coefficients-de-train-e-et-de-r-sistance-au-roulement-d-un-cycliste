import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np
from statistics import mean


#données numériques

g=9.8 #accélération de la pesanteur en m/s-2
rho=1.225 #masse volumique de l'air en kg/m3
Aire=0.5 #aire projetée totale en m²
m=65+15.5 #masse totale en kg
R=6371.009*10**3 #rayon de la Terre en m

#initialisation des listes des résultats
Cr=[]
Cx=[]
VMOYCARRE=[]
ACCMOY=[]
P0=[]
P1=[]

#listes des points de mesure.
T1=[None,12,15,13,14,13,14,13,15,16,11,12,13]
T2=[None,17,18,16,17,16,17,16,18,19,18,16,17]

#il faut encore prendre en compte le décallage dû aux pertes d'informations du GPS
for i in range(1,len(T1)):
    T1[i],T2[i]=T1[i]-2,T2[i]-2
#T1[9]=T1[9]-1
#T1[11]=T1[11]
#T1[12]=T1[12]
#T2[9]=T2[9]-1
#T2[11]=T2[11]
#T2[12]=T2[12]


for i in range (1,13):

    txt_file_path = r'D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_2\\1_bar\\'+str(i)+'.gpx'
    mode_path = r'D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_2\\1_bar\\'+str(i)+'.gpx'
    f = open(txt_file_path,'r')


    LAT=[]
    LON=[]
    ELE=[]
    TEMPS=[]
    DT=[]
    TEMPS_TOT=[0]
    lat_balise="lat=_"
    ele_balise=">ele>"
    temps_balise=">time>"
    balise1="_"
    balise2=">"

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

    #définition des points de mesure
    t1,t2=TEMPS_TOT[T1[i]],TEMPS_TOT[T2[i]]

    #calcul delta-distance
    D=[]
    DTOT=[0]

    for i in range(0,len(LAT)-1):
        d=np.sqrt((LAT[i+1]-LAT[i])**2+(LON[i+1]-LON[i])**2+(ELE[i+1]-ELE[i])**2)
        D.append(d)
        DTOT.append(DTOT[i]+D[i])

    #regression

    TEMPS_TOT=TEMPS_TOT[int(t1):int(t2)]
    DTOT=DTOT[int(t1):int(t2)]

    L=np.polyfit(TEMPS_TOT,DTOT,4)
    t=np.linspace(TEMPS_TOT[0],TEMPS_TOT[-1],len(TEMPS_TOT))


    def position(t):
        return L[0]*t**4+L[1]*t**3+L[2]*t**2+L[3]*t+L[4]

    #plt.plot(t,DTOT,'b--')
    #plt.plot(t,position(t),'r+')
    #plt.show()

    def vitesse(t):
        return (4*L[0]*t**3+3*L[1]*t**2+2*L[2]*t+L[3])

    #plt.plot(t,vitesse(t),'b--')
    #plt.show()

    def acceleration(t):
        return (12*L[0]*t**2+6*L[1]*t+2*L[2])

    #plt.plot(t,acceleration(t),'b--')
    #plt.show()

    VQ=[]
    ACC=[]

    for i in range(0,len(t)):
        VQ.append(vitesse(t[i])**2)
        ACC.append(acceleration(t[i]))

    VQ=np.array(VQ)
    ACC=np.array(ACC)

    VMOYCARRE.append(round(mean(VQ),4))
    ACCMOY.append(round(mean(ACC),4))

    P=np.polyfit(VQ,m*ACC,1)
    #print("m*a = ",P[0],"*v² ",P[1])
    #print("Cr = ",abs(P[1]/(m*g)))
    #print("Cx = ",abs(2*P[0]/(rho*Aire)))
    #print(len(TEMPS_TOT),len(DTOT))

    #VMOYCARRE.append()
    #ACC.append()
    P0.append(round(abs(P[0]),4))
    P1.append(round(abs(P[1]),4))
    Cr.append(round(abs(P[1]/(m*g)),4))
    Cx.append(round(abs(2*P[0]/(rho*Aire)),4))




plt.plot(Cr)
plt.show()
plt.plot(Cx)
plt.show()
print("Cr : ",Cr[1:8])
print("Cx : ",Cx[1:8])
print("ordonnée à l'origine : ",round(mean(P1[1:8]),5))
print("coefficient directeur : ",round(mean(P0[1:8]),5))
print("Crmoy = ",round(mean(Cr[1:8]),5))
print("Cxmoy = ",round(mean(Cx[1:8]),5))
VMOYCARRE=np.array(VMOYCARRE)
ACCMOY=np.array(ACCMOY)
PMOY=np.polyfit(VMOYCARRE,m*ACCMOY,1)
print("ordonnée à l'origine : ",round(PMOY[1],4))
print("coefficient directeur : ",round(PMOY[0],4))
print("Cr méthode Candau : ",round(abs(PMOY[1]/(m*g)),4))
print("Cx méthode Candau : ",round(abs(2*P[0]/(rho*Aire)),4))
plt.plot(VMOYCARRE,PMOY[0]*VMOYCARRE+PMOY[1],"-r")
plt.plot(VMOYCARRE,m*ACCMOY,"bo")
plt.show()
