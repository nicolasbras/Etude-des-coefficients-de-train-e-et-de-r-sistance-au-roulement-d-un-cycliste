# Etude-des-coefficients-de-train-e-et-de-r-sistance-au-roulement-d-un-cycliste
TIPE réalisé dans le contexte de mes études au Lycée Saint Louis en 2023-2024

Objectif : Détermination des coefficients Cx et Cr d'un cycliste par régressions linéaires et autres méthodes, de mesures extraites de relevés par coordonnées GPS grâce à l'application pour smartphone et montres connectées Strava.

Grâce au principe fondamental de la dynamique, qui relie la cinématique et la dynamique du cycliste sur son vélo, on peut remonter aux caractéristiques de l'équipement.

L'étude expérimentale a été réalisée en deux étapes : 

-Mesures en soufflerie pour des casques miniatures modélisés en PLA.
-Mesures cinématiques par suivi GPS du cycliste durant une décélération pure sur terrain plat (la puissance apportée par le cycliste est nulle durant la décélération).

# Remarque importante : pour faire fonctionner les programmes en Python, il est nécéssaire de modifier le chemin d'accès spécifié dans les premières lignes afin que la data soit reconnue.

## Contenu
- `Analyses/` : contient les scripts d'analyse et exploitation des données GPS
- `Mesures.../` : data utile aux programmes
- `Pesage des photographies/` : détermination de la surface utilisée dans les calculs de force de trainée
- `Main programs/` : contient les fichiers Python les plus importants, à l'exception des fichiers d'analyses cinématiques

# Commentaires d'utilisation
Les fichiers Présentation.pdf et "Programmes numériques.pdf" sont prévus pour que l'utilisateur ait une vision complète de l'étude menée, sans avoir recourt à l'exécution des programmes.

Les fichiers contenus dans `Analyses/` sont nombreux et témoignent des nombreuses tentatives d'augmenter la précision dans mes approches de calculs. Différentes méthodes ont été employées et comparées : la dérivation discrète des données brutes, la dérivation de polynomes suivant la courbe les données, et la méthode d'Euler (la méthode RK4 a aussi été testée).

## Conclusions
Bien que ces méthodes mènent toutes aux mêmes conclusions, à savoir que les casques profilés pénètrent mieux dans l'air et que les pneus bien gonflés dissipent moins de puissance, les résultats numériques ne concordent pas assez pour déterminer précisément les valeurs des coefficients Cx et Cr. Des ordres de grandeurs ont pu être relevés mais avec des incertitudes trop fortes. Le matériel employé s'est révélé insuffisant dans ce contexte. Un autre groupe de travail du Lycée Saint Louis s'est proposé de répondre aux mêmes problématiques. La méthode employée fut différente : des capteurs relevant le passage du cycliste à l'aide de cartes Arduino se sont révélés plus précis. Bien que cela ne relève pas de ma propriété intellectuelle, j'ai pu développer l'acquisition des données sur Arduino avec eux. Leur étude en est venue aux mêmes conclusions, avec des valeurs de Cr plus précises.
