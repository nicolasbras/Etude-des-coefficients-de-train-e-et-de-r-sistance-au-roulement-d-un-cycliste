import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd

N = 1000000
rho = 1.293

S1 = 1.392 * 10**-2
S2 = 1.298 * 10**-2
S3 = 1.142 * 10**-2

F10 = 0.155
F20 = 0.135
F30 = 0.12

dF = 0.005  # Écart-type pour la distribution normale

V0 = 7.71
dV = 0.43

F1 = F10 + rd.uniform(-dF, dF, N)
F2 = F20 + rd.uniform(-dF, dF, N)
F3 = F30 + rd.uniform(-dF, dF, N)

V=V0+rd.normal(0,dV,N)

Cx1=2*F1/(rho*S1*V**2)
Cx2=2*F2/(rho*S2*V**2)
Cx3=2*F3/(rho*S3*V**2)

Cx1moy= np.mean(Cx1)
uCx1=np.std(Cx1,ddof=1)
Cx2moy= np.mean(Cx2)
uCx2=np.std(Cx2,ddof=1)
Cx3moy= np.mean(Cx3)
uCx3=np.std(Cx3,ddof=1)

print("Casque sphérique : Cx = ",round(Cx1moy,3),"±",round(uCx1,3))
print("Casque intermédiaire : Cx = ",round(Cx2moy,3),"±",round(uCx2,3))
print("Casque à pointe longue : Cx = ",round(Cx3moy,3),"±",round(uCx3,3))

plt.figure(1)
plt.title("Coefficient de traînée : algorithme de Monte Carlo")

plt.hist(Cx1,bins='rice',color='red',density=True,histtype='stepfilled',label="Casque sphérique")

plt.hist(Cx2,bins='rice',color='blue',density=True,histtype='step',label="Casque intermédiaire")
plt.hist(Cx3,bins='rice',color='green',density=True,histtype='step',label="Casque à pointe longue'")
plt.xlabel("Cx")
plt.ylabel("densité de probabilité")
plt.legend()
plt.show()

