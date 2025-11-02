import matplotlib.pyplot as plt
import numpy as np


polynomeneuf=[[20,0.002681908645],[40,0.02245036649],[40,0.02281442648],[40,0.01941653318]]

simulationneuf=[[20,0.01],[20,0.012],[20,0.008],[40,0.0041],[40,0.0068],[40,0.0013],[40,0.0086],[40,0.0009],[20,0.0161],[20,0.009],[20,0.0113],[20,0.0189],[20,0.0069],[20,0.0161],[20,0.0108],[40,0.0081],[40,0.0063],[40,0.0116]]

simulationneuf2eserie=[[40,0.021],[40,0.018],[40,0.015],[20,0.028],[20,0.03],[20,0.027]]

polynomeancien=[[29,0.01447502548],[29,0.01771151886],[43.5,0.009620285423],[43.5,0.02469],[58,0.0161],[58,0.0152],[58,0.0207],[72.5,0.0285],[72.5,0.0215]]

simulationancien=[[29,0.023],[43.5,0.01],[58,0.006],[14.5,0.0242]]

derivationdiscrete=[[20,0.0451],[20,0.0392],[20,0.021],[40,0.0502],[40,0.0345],[40,0.0332]]

simulationneuf3eserie=[[20,0.0161],[20,0.009],[20,0.0113],[20,0.0189],[20,0.0069],[20,0.0161],[20,0.0108],[40,0.0158],[40,0.0081],[40,0.0219],[40,0.0063],[40,0.0116],[40,-0.0012]]

x1,y1=zip(*polynomeneuf)
x2,y2=zip(*simulationneuf)
x3,y3=zip(*polynomeancien)
x4,y4=zip(*simulationancien)
x5,y5=zip(*simulationneuf2eserie)
x6,y6=zip(*derivationdiscrete)

plt.scatter(x2,y2,label="simulation pneus neufs",s=200)

plt.scatter(x4,y4,label="simulation pneus usés",s=200)

#plt.scatter(x1,y1,s=200)

#plt.scatter(x3,y3,s=200)

#plt.scatter(x5,y5,label="simulation pneus neufs",s=200)

#plt.scatter(x6,y6,s=200)

plt.xlabel("Pression en psi",size=20,)
plt.ylabel("Coefficient de roulement Cr", size=20)

plt.title("Résultats pour la méthode de comparaison à la simulation",fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 22},)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.grid(True)


plt.show()

