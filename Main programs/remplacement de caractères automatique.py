import os
import shutil

def copie(entree,sortie): #Effectue la copie du fichier original
    shutil.copy(entree,sortie)

def remplacer(chemin,ancien_car,nouveau_car): #Remplace les caractères
    with open(chemin,'r') as f:
        texte=f.read()

    texte=texte.replace(ancien_car,nouveau_car)

    with open(chemin,'w') as f:
        f.write(texte)

#Si le chemin n'existe pas, il est créé
sortie="D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_3\\20psiconv"
if not os.path.exists(sortie):
    os.makedirs(sortie)

for i in range(1,4): #Effectue l'opération pour les fichiers nommés 1,2 et 3
    entree=f"D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_3\\20psi\\{i}.gpx"
    sortie=f"D:\\Ecole\\prépa\\psi\\Mesures_pneus_pression_tipe\\mesures_3\\20psiconv\\{i}.gpx"

    #Copie du contenu en entrée vers la sortie
    copie(entree,sortie)

    #Remplacement des caractères dans le fichier de sortie
    remplacer(sortie,'"','_')
    remplacer(sortie,'<','>')
    remplacer(sortie,'Z','>')

