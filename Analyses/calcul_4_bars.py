import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np


#données numériques

g=9.8 #accélération de la pesanteur en m/s-2
rho=1.225 #masse volumique de l'air en kg/m3
Aire=0.5 #aire projetée totale en m²
m=65+15.5 #masse totale en kg
R=6371.009*10**3 #rayon de la Terre en m

#initialisation des listes des résultats
ACC=np.array([])
VMOY=np.array([])

#listes des points de mesure.
T1=[None,16,12,14,13,14,13,14,14,13,12,12,16]
T2=[None,21,15,18,19,19,14,16,16,15,14,14,20]

#il faut encore prendre en compte le décallage dû aux pertes d'informations du GPS
#for i in range(1,len(T1)):
#    T1[i],T2[i]=T1[i]-2,T2[i]-2
T1[9]=T1[9]+1
T1[11]=T1[11]+2
T1[12]=T1[12]+1
T2[9]=T2[9]+1
T2[11]=T2[11]+2
T2[12]=T2[12]+1


for i in range (1,13):

    txt_file_path = r'D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_2\\4_bars\\'+str(i)+'.txt'
    mode_path = r'D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_2\\4_bars\\'+str(i)+'.txt'
    f = open(txt_file_path,'r')

    #with open(file_path, 'w') as file:
        #file.write(modified_content)

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
    t11,t12,t21,t22=TEMPS_TOT[T1[i]],TEMPS_TOT[T1[i]+1],TEMPS_TOT[T2[i]],TEMPS_TOT[T2[i]+1]
    print(i,t11,t12,t21,t22)

    d1,d2=np.sqrt((LAT[T1[i]+1]-LAT[T1[i]])**2+(LON[T1[i]+1]-LON[T1[i]])**2+(ELE[T1[i]+1]-ELE[T1[i]])**2),np.sqrt((LAT[T2[i]+1]-LAT[T2[i]])**2+(LON[T2[i]+1]-LON[T2[i]])**2+(ELE[T2[i]+1]-ELE[T2[i]])**2)

    v1,v2=d1/(t12-t11),d2/(t22-t21)

    dt=(t21+t22-t11-t12)/2

    a=(v2-v1)/dt

    vmoy=(v1+v2)/2

    ACC=np.append(ACC,a)
    VMOY=np.append(VMOY,vmoy)


VMOYCARRE=np.square(VMOY)

plt.plot(VMOYCARRE,m*ACC,"bo")
plt.show()