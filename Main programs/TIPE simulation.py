import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
from scipy.integrate import odeint

#Données
M1=80#ancienne masse
M=84 #masse du vélo+cycliste
g=9.8
Cx=1 #coefficient de trainée
rho=1.225 #masse volumique de l'air
S=0.5 #surface frontale
Cr=0.004 #coefficient de roulement
theta=1*np.pi/180 #angle de la pente

##Données

DTOT2bars=[0, 9.770141404154604, 18.73720631890594, 26.625640404157764, 34.59763775456978, 41.16550202640981, 47.43201341154522, 52.90300225107431, 58.728818205329375, 64.11805286998035, 68.64685919564339, 72.52595830051098, 76.45572533742616, 79.8898514783125]
TEMPS_TOT2bars=[0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]

#DTOT3bars=[23.300670970422168, 27.102191308460533, 30.618488600486856, 33.307938876397564, 36.08781596942212, 36.83373526771844, 37.48977473665885, 38.15694523899159]
#TEMPS_TOT3bars=[6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]

DTOT3bars=[23.300670970422168, 27.102191308460533, 30.618488600486856, 33.307938876397564, 36.08781596942212]
TEMPS_TOT3bars=[6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars=[0, 7.8884340852518235, 15.860431435663843, 22.42829570750387, 28.69480709263928, 34.165795932168365, 39.99161188642343, 45.38084655107439, 49.90965287673743, 53.788751981605024, 57.71851901852021, 61.152645159406546]
TEMPS_TOT4bars=[0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]

#DTOT4bis=[0, 8.504061589947792, 16.667483915762276, 24.763225834391697, 32.38475458778799, 38.62060819363024, 45.68548632842145, 51.2561367149718, 56.34809458166147, 61.124060998097406, 64.91938230773297, 69.44571883834533, 73.14336715064083, 76.80099248258578, 80.07133800670618, 83.34168353082659]
#TEMPS_TOT4bis=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]

DTOT4bis=[38.62060819363024, 45.68548632842145, 51.2561367149718, 56.34809458166147, 61.124060998097406, 64.91938230773297, 69.44571883834533, 73.14336715064083]
TEMPS_TOT4bis=[6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0]

DTOT4bars1=[0, 8.01839151906857, 15.685862024160567, 22.40649877188655, 28.876867983624308]
TEMPS_TOT4bars1=[1.0, 2.0, 3.0, 4.0, 5.0]

DTOT4bars2=[0, 7.455877045350156, 13.740916677805863, 19.621654519582602, 25.400590432758637]
TEMPS_TOT4bars2=[1.0, 2.0, 3.0, 4.0, 5.0]

DTOT4bars3=[0, 9.493878169091754, 19.07280381066254, 26.90223969815964, 34.5690580705173, 41.07658350311489, 48.43044560910884, 55.47182544850877, 59.446655088178645]
TEMPS_TOT4bars3=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

DTOT4bars4=[0, 7.178760116665224, 13.869719304334406, 20.27092581422799, 26.824836115850573, 33.17154211351824, 38.997358068219924, 44.412912540559326, 49.16422105776886, 54.02129562967366, 58.363602462744055, 61.478670322206135]
TEMPS_TOT4bars4=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT4bars5=[0, 7.2105532133849, 14.045939202843904, 20.736151071356886, 25.83781253492358, 31.2325606899107, 36.44095550379938, 41.191211562761666, 44.994668618379656, 48.58544140497025, 51.79472493165199, 54.46803605463774, 56.59241514623282, 58.23419088208078]
TEMPS_TOT4bars5=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]

DTOT4bars6=[0, 8.446435943119882, 16.435327795576267, 23.785146194189608, 30.57242777437662, 37.78298098743389, 44.82436082689402, 50.192687166024434, 54.5915736728795, 57.61640697685436]
TEMPS_TOT4bars6=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars7=[0, 10.302811070051902, 20.475677778603483, 30.403848377850892, 39.825168891079, 48.21284630554137, 54.6973492617424, 61.710408979469854, 67.42804245230167, 70.66763593825664]
TEMPS_TOT4bars7=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars8=[0, 10.172375193447897, 19.12672741100577, 28.163679861083814, 36.63204514245088, 44.755992338569506, 52.25238850582257, 60.049383318264816, 65.50226231313644, 68.10527248618095]
TEMPS_TOT4bars8=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars9=[0, 12.234394800263804, 23.508945057708594, 33.758815956440124, 44.413724052647, 54.40891894271276, 63.957339115880636, 72.60771632698123, 80.16979958681911, 84.60089228198308, 87.16803013598437, 88.54343736242913, 90.43702140503241, 93.33023115865714, 97.00640184048802, 101.56540027317989]
TEMPS_TOT4bars9=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]

DTOT4bars10=[0, 9.978982088897657, 20.6872476243364, 31.447811828020313, 41.26892521555287, 50.271476404260284, 58.397851698980006, 65.92372092651028, 73.8708639765373, 81.5084436406021, 89.28081994107913, 95.2149297515368]
TEMPS_TOT4bars10=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT4bars11=[0, 11.301933500226811, 21.686625668382135, 31.50824815047301, 40.582748062369774, 49.186408853645474, 57.38850676184404, 64.16393698741936, 68.1731327471498, 70.46547812356482]
TEMPS_TOT4bars11=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars12=[0, 7.982698682607646, 16.143236105421195, 23.96966397991173, 31.49553320768969, 38.74456578014666, 45.12545862546775, 50.74912596696293, 56.48942071601054]
TEMPS_TOT4bars12=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

LT=[TEMPS_TOT4bars1,TEMPS_TOT4bars2,TEMPS_TOT4bars3,TEMPS_TOT4bars4,TEMPS_TOT4bars5,TEMPS_TOT4bars6,TEMPS_TOT4bars7,TEMPS_TOT4bars8,TEMPS_TOT4bars9,TEMPS_TOT4bars10,TEMPS_TOT4bars11,TEMPS_TOT4bars12]
LD=[TEMPS_TOT4bars1,TEMPS_TOT4bars2,TEMPS_TOT4bars3,TEMPS_TOT4bars4,TEMPS_TOT4bars5,TEMPS_TOT4bars6,TEMPS_TOT4bars7,TEMPS_TOT4bars8,TEMPS_TOT4bars9,TEMPS_TOT4bars10,TEMPS_TOT4bars11,TEMPS_TOT4bars12]




DTOT20psi1=[7.913622163538733, 15.58205307504593, 22.517104920463442, 29.344519280860048, 35.65606113222654, 41.35419892333825, 46.61338550003546, 51.442132068399275, 56.05505311418548, 60.28923575507805]

TEMPS_TOT20psi1=[2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]

DTOT20psi2=[0, 9.565362783015487, 18.0765520443194, 26.501735371024015, 34.28618544163287, 41.640047547923416, 48.74436053379993, 55.487779741298596, 62.31592640434493, 68.18403558909975, 71.50281074190744]

TEMPS_TOT20psi2=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]

DTOT20psi3=[91.89539616300742, 94.39419488546137, 96.9805265610597, 99.23205540222602, 100.85108025981145]

TEMPS_TOT20psi3=[32.0, 33.0, 34.0, 35.0, 36.0]




DTOT40psi1=[77.0471195408489, 85.87645731842237, 94.56805059317196, 103.19911011877284, 110.65565774538418, 117.80421317152441, 124.84822645132465]

TEMPS_TOT40psi1=[17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0]

DTOT40psi2=[43.02146375768431, 54.754420383768775, 66.38108808658114, 77.04295652974012, 86.82053947501377, 96.8778927826605, 106.0922079530244, 114.35737674796712, 121.95356272786715, 127.83935366516205]

TEMPS_TOT40psi2=[5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]

DTOT40psi3=[15.283924276584635, 26.687688289113595, 37.97549552372266, 48.17324798606921, 58.76716956812475, 68.34855305373887, 77.0424158913949, 85.01504041180081, 92.68347132322445, 100.56563330716587, 107.32021983163071, 113.84671768206046, 120.18660148173849, 126.34263287093934, 132.04164807451212]

TEMPS_TOT40psi3=[28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0]

DTOT40psi4=[60.16383557363731, 71.9451678870685, 83.24217730199341, 93.83609888404895, 103.19024859730455, 112.89548392337255, 121.69382524416669, 130.20501450547061, 138.11863666958678, 145.6813810937239, 150.7633842220559]

TEMPS_TOT40psi4=[6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]

DTOT40psi5=[70.15594811503108, 75.30705361762745, 80.30217639171786, 84.80797900520017, 89.20800201600761, 93.32222011373835, 97.25198715025826, 101.18302632050377, 104.22009770488258, 107.30363180949112, 110.3646464143657, 113.03795753683696, 115.95669610641956, 117.54876741854031]

TEMPS_TOT40psi5=[11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]
## PREMIERE SERIE DE MESURES
DTOT=[110.52626356041387, 119.15790236976332, 127.4702351354184, 136.72837212480732, 146.64422768412234, 156.41436908827694, 165.3814340030283, 173.2698680882801, 181.24186543869212, 187.80972971053214, 194.07624109566754, 199.54722993519664]
TEMPS_TOT=[94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0]
##
##
##
##                                                                  SERIE 4 BARS
##
DTOT4bars1=[0, 10.303296362428489, 19.34024881274933, 28.810127704027764, 38.23538453293432, 47.14002124832098, 56.28294109452318, 64.30133261359175, 71.96880311868375, 78.68943986640974, 85.1598090781475, 90.99814268896893]
TEMPS_TOT4bars1=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT4bars2=[13.740916677805863, 19.621654519582602, 25.400590432758637]
TEMPS_TOT4bars2=[3.0, 4.0, 5.0]

DTOT4bars3=[19.07280381066254, 26.90223969815964, 34.5690580705173, 41.07658350311489, 48.43044560910884, 55.47182544850877, 59.446655088178645]
TEMPS_TOT4bars3=[3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

DTOT4bars4=[0, 7.178760116665224, 13.869719304334406, 20.27092581422799, 26.824836115850573, 33.17154211351824, 38.997358068219924, 44.412912540559326, 49.16422105776886, 54.02129562967366, 58.363602462744055, 61.478670322206135]
TEMPS_TOT4bars4=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT4bars5=[0, 7.2105532133849, 14.045939202843904, 20.736151071356886, 25.83781253492358, 31.2325606899107, 36.44095550379938, 41.191211562761666, 44.994668618379656, 48.58544140497025, 51.79472493165199, 54.46803605463774, 56.59241514623282, 58.23419088208078]
TEMPS_TOT4bars5=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]

DTOT4bars6=[0, 8.446435943119882, 16.435327795576267, 23.785146194189608, 30.57242777437662, 37.78298098743389, 44.82436082689402, 50.192687166024434, 54.5915736728795, 57.61640697685436]
TEMPS_TOT4bars6=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars7=[0, 10.302811070051902, 20.475677778603483, 30.403848377850892, 39.825168891079, 48.21284630554137, 54.6973492617424, 61.710408979469854, 67.42804245230167, 70.66763593825664]
TEMPS_TOT4bars7=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars8=[0, 10.172375193447897, 19.12672741100577, 28.163679861083814, 36.63204514245088, 44.755992338569506, 52.25238850582257, 60.049383318264816, 65.50226231313644, 68.10527248618095]
TEMPS_TOT4bars8=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars9=[0, 12.234394800263804, 23.508945057708594, 33.758815956440124, 44.413724052647, 54.40891894271276, 63.957339115880636, 72.60771632698123, 80.16979958681911, 84.60089228198308, 87.16803013598437, 88.54343736242913, 90.43702140503241, 93.33023115865714, 97.00640184048802, 101.56540027317989]
TEMPS_TOT4bars9=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]

DTOT4bars10=[0, 9.978982088897657, 20.6872476243364, 31.447811828020313, 41.26892521555287, 50.271476404260284, 58.397851698980006, 65.92372092651028, 73.8708639765373, 81.5084436406021, 89.28081994107913, 95.2149297515368]
TEMPS_TOT4bars10=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

DTOT4bars11=[0, 11.301933500226811, 21.686625668382135, 31.50824815047301, 40.582748062369774, 49.186408853645474, 57.38850676184404, 64.16393698741936, 68.1731327471498, 70.46547812356482]
TEMPS_TOT4bars11=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

DTOT4bars12=[0, 7.982698682607646, 16.143236105421195, 23.96966397991173, 31.49553320768969, 38.74456578014666, 45.12545862546775, 50.74912596696293, 56.48942071601054]
TEMPS_TOT4bars12=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

LT=[TEMPS_TOT4bars1,TEMPS_TOT4bars2,TEMPS_TOT4bars3,TEMPS_TOT4bars4,TEMPS_TOT4bars5,TEMPS_TOT4bars6,TEMPS_TOT4bars7,TEMPS_TOT4bars8,TEMPS_TOT4bars9,TEMPS_TOT4bars10,TEMPS_TOT4bars11,TEMPS_TOT4bars12]
LD=[TEMPS_TOT4bars1,TEMPS_TOT4bars2,TEMPS_TOT4bars3,TEMPS_TOT4bars4,TEMPS_TOT4bars5,TEMPS_TOT4bars6,TEMPS_TOT4bars7,TEMPS_TOT4bars8,TEMPS_TOT4bars9,TEMPS_TOT4bars10,TEMPS_TOT4bars11,TEMPS_TOT4bars12]
##

##SERIE 1 BAR
TEMPS_TOT1bar1=[12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
DTOT1bar1=[67.47168662139585, 76.37410750792164, 84.46923179437046, 92.26320607388226, 99.16877778517981, 105.22048785452064, 110.77801769403303, 115.664037446684]
##
TEMPS_TOT1bar2=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
DTOT1bar2=[0, 1.2281898430050515, 1.2281898430050515, 3.8240652100315833, 7.575148584395151, 13.115753999948952, 21.100149487464567, 29.302247395130085, 38.059034108846454, 48.12449268768563, 58.78636113061028, 67.47168662139585, 76.37410750792164, 84.46923179437046, 92.26320607388226, 99.16877778517981, 105.22048785452064, 110.77801769403303, 115.664037446684]

TEMPS_TOT1bar3=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
DTOT1bar3=[0, 1.2281898430050515, 1.2281898430050515, 3.8240652100315833, 7.575148584395151, 13.115753999948952, 21.100149487464567, 29.302247395130085, 38.059034108846454, 48.12449268768563, 58.78636113061028, 67.47168662139585, 76.37410750792164, 84.46923179437046, 92.26320607388226, 99.16877778517981, 105.22048785452064, 110.77801769403303, 115.664037446684]

TEMPS_TOT1bar4=
DTOT1bar4=

TEMPS_TOT1bar5=
DTOT1bar5=

TEMPS_TOT1bar6=
DTOT1bar6=

TEMPS_TOT1bar7=
DTOT1bar7=

TEMPS_TOT1bar8=
DTOT1bar8=

TEMPS_TOT1bar9=
DTOT1bar9=

TEMPS_TOT1bar10=
DTOT1bar10=

TEMPS_TOT1bar11=
DTOT1bar11=

TEMPS_TOT1bar12=
DTOT1bar12=



##Fonction 20 psi 1
Cr=0.031
Cx=0.95
TI=TEMPS_TOT[0]
TF=TEMPS_TOT[-1]
N=100
T=(TF-TI)/N
x0=DTOT[0]
v0=(DTOT[1]-DTOT[0])/(TEMPS_TOT[1]-TEMPS_TOT[0])

def dichotomie1(P,app,N,T,x0,v0):
    m=0
    Cx=0.5
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M1-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT[-1]<X1[-1]:
            Cx+=app
        else:
            Cx-=app
        print(m,"Cx = ",round(Cx,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur : ',abs(round(DTOT[-1]-X1[-1],3)))
    return round(Cx,6)

plt.close()
def dichotomie2(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M1-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur  : ',abs(round(DTOT[-1]-X1[-1],3)))
    return round(Cr,6)



Cx=dichotomie1(50,1/2000,N,T,x0,v0)
Cr=dichotomie2(50,1/2000,N,T,x0,v0)


plt.plot(TEMPS_TOT,DTOT,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()
print("Cr = ",Cr)
print("Cx = ",Cx)
##Fonctions 2 bars

Cr=0.045
Cx=0.8

TF=TEMPS_TOT2bars[-1]
N=100
T=TF/N
x0=DTOT2bars[0]
v0=(DTOT2bars[1]-DTOT2bars[0])/TEMPS_TOT2bars[1]

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(0,TF,N)
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
t=np.linspace(0,TF,N+1)
ODEINT=odeint(F,np.array([x0,v0]),t)
X1=[]
for i in range(0,len(ODEINT)):
    X1.append(ODEINT[i][0])

plt.close()
for j in range(0,10):
    #Cx+=i/100
    Cx+=j/20
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT2bars,DTOT2bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

##Dichotomie 2 bars
Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT2bars[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,7))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT2bars[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(100,1/10000,N,T,x0,v0)

plt.plot(TEMPS_TOT2bars,DTOT2bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()


##Fonctions 3 bars
Cr=0.020
Cx=0.8

TI=TEMPS_TOT3bars[0]
TF=TEMPS_TOT3bars[-1]
N=100
T=(TF-TI)/N
x0=DTOT3bars[0]
v0=(DTOT3bars[1]-DTOT3bars[0])/(TEMPS_TOT3bars[1]-TEMPS_TOT3bars[0])

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
for j in range(0,10):
    #Cx+=i/100
    Cr+=j/1000
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT3bars,DTOT3bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

##Dichotomie 3 bars
Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT3bars[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT3bars[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT3bars,DTOT3bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonctions 4 bars

Cr=0.031
Cx=0.8

TF=TEMPS_TOT4bars[-1]
N=100
T=TF/N
x0=DTOT4bars[0]
v0=(DTOT4bars[1]-DTOT4bars[0])/TEMPS_TOT4bars[1]

def F(X,t):
    dXdt=X[1]
    dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
    return [dXdt,dVdt]

def euler(F,x0,v0,T,N):
    temps = np.linspace(0,TF,N)
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
t=np.linspace(0,TF,N+1)
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
plt.plot(TEMPS_TOT4bars,DTOT4bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT4bars[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT4bars[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT4bars,DTOT4bars,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonctions 4 bars bis
Cr=0.031
Cx=0.8

TI=TEMPS_TOT4bis[0]
TF=TEMPS_TOT4bis[-1]
N=100
T=(TF-TI)/N
x0=DTOT4bis[0]
v0=(DTOT4bis[1]-DTOT4bis[0])/(TEMPS_TOT4bis[1]-TI)

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
for j in range(0,10):
    #Cx+=i/100
    Cr+=j/500
    XA,VA=euler(F,x0,v0,T,N)
    plt.plot(t,XA,color=np.random.rand(3,),label=1+j)
    print(j+1,' : Cr = ',round(Cr,4),'Cx = ',round(Cx,4))

XA,VA=euler(F,x0,v0,T,N)
plt.plot(t,XA,color=np.random.rand(3,),label='LA')


plt.plot(t,X,'b-',label='Euler')
plt.plot(t,X1,'g--',label='Odeint')
plt.plot(TEMPS_TOT4bis,DTOT4bis,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT4bis[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT4bis[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT4bis,DTOT4bis,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonctions 4 bars 1

Cr=0.031
Cx=0.8

TI=TEMPS_TOT4bars1[0]
TF=TEMPS_TOT4bars1[-1]
N=100
T=(TF-TI)/N
x0=DTOT4bars1[0]
v0=(DTOT4bars1[1]-DTOT4bars1[0])/(TEMPS_TOT4bars1[1]-TEMPS_TOT4bars1[0])

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
plt.plot(TEMPS_TOT4bars1,DTOT4bars1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT4bars1[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT4bars1[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT4bars1,DTOT4bars1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonctions 4 bars 2
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT4bars"+'i'
TI=TEMPS_TOT4bars2[0]
TF=TEMPS_TOT4bars2[-1]
N=100
T=(TF-TI)/N
x0=DTOT4bars2[0]
v0=(DTOT4bars2[1]-DTOT4bars2[0])/(TEMPS_TOT4bars2[1]-TEMPS_TOT4bars2[0])

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
plt.plot(TEMPS_TOT4bars2,DTOT4bars2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT4bars2[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT4bars2[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT4bars2,DTOT4bars2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonctions 4 bars 2eme série de mesures
for k in range(0,4):
    Cr=0.031
    Cx=0.2
    TEMPS_TOT=LT[k]
    DTOT=LD[k]
    TI=TEMPS_TOT[0]
    TF=TEMPS_TOT[-1]
    N=100
    T=(TF-TI)/N
    x0=DTOT[0]
    v0=(DTOT[1]-DTOT[0])/(TEMPS_TOT[1]-TEMPS_TOT[0])

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
    plt.plot(TEMPS_TOT,DTOT,'r+',label='Expérimentale')
    plt.xlabel("temps en s")
    plt.ylabel("distance en m")
    plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
    plt.show()

    Cr=0.02
    Cx=0.2

    plt.close()
    def dichotomie(P,app,N,T,x0,v0):
        m=0
        Cr=0.03
        while m<P:
            def F(X,t):
                dXdt=X[1]
                dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
                return [dXdt,dVdt]
            ODEINT=odeint(F,np.array([x0,v0]),t)
            X1=[]
            for i in range(0,len(ODEINT)):
                X1.append(ODEINT[i][0])
            if DTOT[-1]<X1[-1]:
                Cr+=app
            else:
                Cr-=app
            print(m,"Cr = ",round(Cr,4))

            plt.plot(t,X1,color=np.random.rand(3,))
            m+=1
            print('Mesure n°',k+1,'erreur : ',abs(round(DTOT[-1]-X1[-1],3)))
        return round(Cr,6)

    dichotomie(50,1/1000,N,T,x0,v0)

    plt.plot(TEMPS_TOT,DTOT,'r+',label='Expérimentale n°')
    plt.xlabel("temps en s")
    plt.ylabel("distance en m")
    plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
    plt.show()

##FONCTION 20 PSI 1 SAVE
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
plt.plot(TEMPS_TOT20psi1,DTOT20psi1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()
##Fonction 20 psi 1

DTOT20psi1=[7.913622163538733, 15.58205307504593, 22.517104920463442, 29.344519280860048, 35.65606113222654, 41.35419892333825, 46.61338550003546, 51.442132068399275, 56.05505311418548, 60.28923575507805]

TEMPS_TOT20psi1=[2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]

t=np.linspace(TI,TF,N+1)

for i in range(0,len(TEMPS_TOT20psi1)):
    TEMPS_TOT20psi1[i]=TEMPS_TOT20psi1[i]-2.0

TI=TEMPS_TOT20psi1[0]
TF=TEMPS_TOT20psi1[-1]
N=100
T=(TF-TI)/N
x0=DTOT20psi1[0]
v0=(DTOT20psi1[1]-DTOT20psi1[0])/(TEMPS_TOT20psi1[1]-TEMPS_TOT20psi1[0])

Cx=1.1966

plt.close()
def dichotomie(P,app,N,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT20psi1[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,6))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT20psi1[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(500,1/10000,N,x0,v0)

plt.plot(TEMPS_TOT20psi1,DTOT20psi1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()
##Fonction 20 psi 2
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT20psi2"
TI=TEMPS_TOT20psi2[0]
TF=TEMPS_TOT20psi2[-1]
N=100
T=(TF-TI)/N
x0=DTOT20psi2[0]
v0=(DTOT20psi2[1]-DTOT20psi2[0])/(TEMPS_TOT20psi2[1]-TEMPS_TOT20psi2[0])

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
plt.plot(TEMPS_TOT20psi2,DTOT20psi2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Descente de gradient', title_fontsize='large')
plt.show()

Cr=0.02
Cx=0.8

plt.close()
def dichotomie(P,app,N,T,x0,v0):
    m=0
    Cr=0.04
    while m<P:
        def F(X,t):
            dXdt=X[1]
            dVdt=-((1/2)*Cx*rho*(X[1]**2)*S)/M-g*(Cr+np.sin(theta))
            return [dXdt,dVdt]
        ODEINT=odeint(F,np.array([x0,v0]),t)
        X1=[]
        for i in range(0,len(ODEINT)):
            X1.append(ODEINT[i][0])
        if DTOT20psi2[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur : ',abs(round(DTOT20psi2[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(400,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT20psi2,DTOT20psi2,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()
##Fonction 20 psi 3
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT20psi3"
TI=TEMPS_TOT20psi3[0]
TF=TEMPS_TOT20psi3[-1]
N=100
T=(TF-TI)/N
x0=DTOT20psi3[0]
v0=(DTOT20psi3[1]-DTOT20psi3[0])/(TEMPS_TOT20psi3[1]-TEMPS_TOT20psi3[0])

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
plt.plot(TEMPS_TOT20psi3,DTOT20psi3,'r+',label='Expérimentale')
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
        if DTOT20psi3[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur en mètres (par rapport à la dernière position) : ',abs(round(DTOT20psi3[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(50,1/1000,N,T,x0,v0)

plt.plot(TEMPS_TOT20psi3,DTOT20psi3,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()

##Fonction 40 psi 1
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
        print('erreur : ',abs(round(DTOT40psi5[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(500,1/10000,N,T,x0,v0)

plt.plot(TEMPS_TOT40psi5,DTOT40psi5,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()
##Fonction 1 bar 1
Cr=0.031
Cx=0.8
TEMPS_TOT="TEMPS_TOT1bar1"
TI=TEMPS_TOT1bar1[0]
TF=TEMPS_TOT1bar1[-1]
N=100
T=(TF-TI)/N
x0=DTOT1bar1[0]
v0=(DTOT1bar1[1]-DTOT1bar1[0])/(TEMPS_TOT1bar1[1]-TEMPS_TOT1bar1[0])

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
plt.plot(TEMPS_TOT1bar1,DTOT1bar1,'r+',label='Expérimentale')
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
        if DTOT1bar1[-1]<X1[-1]:
            Cr+=app
        else:
            Cr-=app
        print(m,"Cr = ",round(Cr,4))

        plt.plot(t,X1,color=np.random.rand(3,))
        m+=1
        print('erreur : ',abs(round(DTOT1bar1[-1]-X1[-1],3)))
    return round(Cr,6)

dichotomie(200,1/10000,N,T,x0,v0)

plt.plot(TEMPS_TOT1bar1,DTOT1bar1,'r+',label='Expérimentale')
plt.xlabel("temps en s")
plt.ylabel("distance en m")
plt.legend(loc='upper left', title='Dichotomie', title_fontsize='large')
plt.show()