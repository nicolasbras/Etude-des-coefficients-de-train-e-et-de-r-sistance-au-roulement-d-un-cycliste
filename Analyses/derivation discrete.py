##Données
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
from scipy.integrate import odeint

#Données
M=84 #masse du vélo+cycliste
g=9.81 #accélération de la pesanteur
rho=1.212 #masse volumique de l'air
S=0.5644 #surface frontale
theta=0*np.pi/180 #angle de la pente

#Mesures

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




DTOT20psi1=[0, 7.913622163538733, 15.58205307504593, 22.517104920463442, 29.344519280860048, 35.65606113222654, 41.35419892333825, 46.61338550003546, 51.442132068399275, 56.05505311418548, 60.28923575507805, 62.79791119057468]

TEMPS_TOT20psi1=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT20psi2=[0, 9.565362783015487, 18.0765520443194, 26.501735371024015, 34.28618544163287, 41.640047547923416, 48.74436053379993, 55.487779741298596, 62.31592640434493, 68.18403558909975, 71.50281074190744]

TEMPS_TOT20psi2=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]

DTOT20psi3=[73.17662324995837, 77.57550975661039, 81.48763153372684, 85.46120305871266, 88.91004365688137, 91.89539616300742, 94.39419488546137, 96.9805265610597, 99.23205540222602, 100.85108025981145]

TEMPS_TOT20psi3=[27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0]

##
def filtrer_donnees_moyennage(liste, taille_fenetre=3):
    """
    Filtre les données en utilisant un filtre de moyennage.

    Paramètres:
    liste (list): Une liste de valeurs numériques.
    taille_fenetre (int): La taille de la fenêtre de moyennage.

    Retourne:
    list: Une nouvelle liste représentant les valeurs lissées.
    """
    fenetre = np.ones(taille_fenetre) / taille_fenetre
    liste_lissee = np.convolve(liste, fenetre, mode='valid')

    # Ajouter les points de bord pour garder la même longueur que la liste originale
    pad_size = (taille_fenetre - 1) // 2
    liste_lissee = np.pad(liste_lissee, (pad_size, pad_size), mode='edge')

    return liste_lissee.tolist()
##
def derivee_discrete(liste):
    n = len(liste)
    if n < 3:
        raise ValueError("La liste doit contenir au moins trois éléments pour utiliser les différences centrées.")
    derivee = [(liste[i + 1] - liste[i - 1]) / 2 for i in range(1, n - 1)]
    derivee = [(liste[1] - liste[0])] + derivee + [(liste[-1] - liste[-2])]
    return derivee

Dfiltre=filtrer_donnees_moyennage(DTOT40psi5,6)
V=derivee_discrete(DTOT40psi5)
Vl=derivee_discrete(Dfiltre)
ACC=derivee_discrete(V)
ACCl=derivee_discrete(Vl)

MACCl=[ACCl[i]*M for i in range(0,len(ACCl))]
VQl=[Vl[i]**2 for i in range(0,len(Vl))]
MACC=[ACC[i]*M for i in range(0,len(ACC))]
VQ=[V[i]**2 for i in range(0,len(V))]
##
plt.plot(TEMPS_TOT40psi5,DTOT40psi5,marker='x')
plt.xlabel("temps en s",size=20)
plt.ylabel("Distance parcourue en m", size=20)

plt.title("Distance parcourue en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
##
plt.plot(TEMPS_TOT40psi5,V)
plt.title("Vitesse en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22},)
plt.xlabel("temps en s",size=20,)
plt.ylabel("Vitesse en m/s", size=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
##
plt.plot(TEMPS_TOT40psi5,ACC)
plt.xlabel("temps en s",size=20)
plt.ylabel("accélération en m/s²",size=20)
plt.title("Accélération en fonction du temps",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
##
plt.plot(VQ,MACC, marker='x')
del VQl[-5:]
del MACCl[-5:]
del VQl[:4]
del MACCl[:4]

P=np.polyfit(VQ,MACC,1)
Cr=abs(P[1]/(M*g))
print("Cr = ",round(Cr,4))
P=np.polyfit(VQl,MACCl,1)
Cr=abs(P[1]/(M*g))
Cx=abs(2*P[0]/(rho*S))
print("Cr = ",round(Cr,4),"  (Après lissage)")
print("Cx = ",round(Cx,4),"  (Après lissage)")

plt.plot(VQl,MACCl)
plt.xlabel("vitesse au carré",size=20)
plt.ylabel("masse*accélération en kg.m/s²",size=20)
plt.title("Masse*accélération en fonction de la vitesse au carré",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22})
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()