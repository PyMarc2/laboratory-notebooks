| **Ludovick Bégin - 111 159 148** |         Date de préparation: 9 février 2020 |
| -------------------------------- | ------------------------------------------: |
| **Coéquipier:** Lucas Wagner     | **Date d'expérimentation: 10 février 2020** |

## Caractérisation d’un imageur tomographique

Le but de ce laboratoire est d'abord de caractériser un imageur tomographique en mesurant les coefficients d'atténuation, la linéarité, la dépendance à l'énergie du rayonnement, la résolution et la fonction de transfert de modulation. De plus, les géométries à faisceau conique et éventail seront comparés et une étude du contraste sur bruit sera faite dans différentes conditions d'imagerie. 

La tomodensitométrie est ici basée sur l'absorption des rayons X. Plusieurs images 2D sont prises par le scanneur DeskCAT à différents angles d'incidence autour du sujet afin d'en reconstruire une image 3D de l'atténuation des tissus face aux rayons X. L'algorithme de reconstruction additionne le signal des projections planes normalisé par l'atténuation spatiale suivant l'équation![image-20200210001124585](C:\Users\MonteaCristo\AppData\Roaming\Typora\typora-user-images\image-20200210001124585.png)Où $N/N_0$ est le taux de photons transmis sur les photons incidents à un objet de longueur x et de coefficient d’atténuation μ.

![image-20200210004128192](C:\Users\MonteaCristo\AppData\Roaming\Typora\typora-user-images\image-20200210004128192.png)



### Méthode

##### Partie 1 - Coefficient d’atténuation, linéarité et énergie

Mesurer les coefficients d'atténuation 3D et 2D pour une acquisition faite sur un bocal d'eau distillée. Prendre d'autres séries de données en ajoutant graduellement (1ml à 15ml) de la solution opaque de colorant. Déterminer la linéarité du coefficient d'atténuation mesuré en fonction de l'ajout de la solution opaque. Faire une série de ces mesures avec la lumière rouge et une autre avec la verte. 

- Shutter Speed à 15.89 fps
- Autocalibration géométrique
- Scan de référence avec bocal d'eau (320 projections et 0.5mm voxels)
- Scan de données avec ce même bocal
- Mode de projection 2D Io/I = 1/$e^{-\mu x}$ pour x = 7 cm

> Io/I

> 1.0018 $\pm$ 0.0035 
>
> 2.1142 (0.0091)
>
> 7.2354 (+7.3073)
>
> 15.4447 (+15.6574)
>
> 22.5545 (+)
>
> 24.1743 (+24.7017)
>
> 26.4175 (+27.0267)
>
> 26.0424 (+26.7098)

*Lumière rouge*

| Solution opaque [ml $\pm$ 0.5] | $\mu_{3D}$ [cm$^{-1}$] | $\mu_{2D}$ [cm$^{-1}$] |
| ------------------------------ | ---------------------- | ---------------------- |
| 0 $\pm$ 0                      | 0.0005 $\pm$ 0.0008    | 0.00026 $\pm$ 0.00001  |
| 1                              | 0.0902 $\pm$ 0.0030    | 0.107                  |
| 3                              | 0.2259 $\pm$ 0.0059    | 0.2827                 |
| 5                              | 0.2744 $\pm$ 0.0114    | 0.3910                 |
| 8                              | 0.2717 $\pm$ 0.0166    | 0.4451                 |
| 10                             | 0.2627 $\pm$ 0.0181    | 0.4550                 |
| 13                             | 0.2572 $\pm$ 0.0192    | 0.4677                 |
| 15                             | 0.2503 $\pm$ 0.0197    | 0.4657                 |
|                                |                        |                        |



*Lumière verte*

- Shutter speed 18.93 fps
- Switch brisée
- Autre DeskCat autocalibre pas et perte communication moteur pour un temps. Passe à la prochaine étape. 

| Solution opaque [ml] | $\mu_{3D}$ [cm$^{-1}$] | $\mu_{2D}$ [cm$^{-1}$] |
| -------------------- | ---------------------- | ---------------------- |
| 0                    |                        |                        |
|                      |                        |                        |
|                      |                        |                        |
|                      |                        |                        |

##### Partie 2 - Faisceau conique et faisceau en éventail

Mesurer les coefficients d'atténuation des structures d'un fantôme et quantifier l'effet de la variation de la largeur du faisceau éventail sur ces mesures. Effectuer la première acquisition et calibration sans diaphragme, puis poursuivre avec les diaphragmes de 0.5, 1.0 et 1.5 cm. 

> Changement de DeskCat !

- On garde la lumière verte
- Référence sur bocal d'eau
- On insère le fantôme à colonnes et note les $\mu$. 

| Diaphragme [cm] | \# Structure | $\mu$ [m$^{-1}$]    |
| --------------- | ------------ | ------------------- |
| 0               | 1 (gros)     | 1.098 $\pm$ 0.051   |
| 0               | 2            | 1.0545 $\pm$ 0.0911 |
| 0               | 3            | 0.9898 $\pm$ 0.1478 |
| 0               | 4            | 0.9927 $\pm$ 0.0939 |
| 0.5             | 1            | 1.3577 $\pm$ 0.0506 |
| 0.5             | 2            | 1.3292 $\pm$ 0.0590 |
| 0.5             | 3            | 1.3275 $\pm$ 0.0836 |
| 0.5             | 4            | 1.2556 $\pm$ 0.1333 |
| 1.0             | 1            | 1.2544 $\pm$ 0.0136 |
| 1.0             | 2            | 1.2086 $\pm$ 0.0669 |
| 1.0             | 3            | 1.1300 $\pm$ 0.1522 |
| 1.0             | 4            | 1.1430 $\pm$ 0.0932 |
| 1.5             | 1            | 1.1941 $\pm$ 0.0097 |
| 1.5             | 2            | 1.1583 $\pm$ 0.048  |
| 1.5             | 3            | 1.1529 $\pm$ 0.0274 |
| 1.5             | 4            | 1.0487 $\pm$ 0.1171 |

- Hauteur des objets:
  - À 0.5 cm: 12.1 pixels (6.05 mm)
  - À 1.0 cm: 22 pixels (11 mm)
  - À 1.5 cm: 29.8 pixels (14.9 mm)

##### Partie 3 - Rapport contraste sur bruit

Selon le contraste sur bruit (CNR) suivant,

![image-20200210010127276](C:\Users\MonteaCristo\AppData\Roaming\Typora\typora-user-images\image-20200210010127276.png)

en mesurer la valeur pour un ensemble de structures coniques d'un fantôme à contraste variable à l'aide de la lumière verte. Comparer la visibilité en fonction de la taille, de l'atténuation et du niveau de bruit. Faire ces manipulations d'abord avec un faisceau conique et ensuite avec le faisceau éventail de 1cm. 

- Luminosité à 50%
- Scan de référence sur le *blank silicone*
- Ajout du fantôme *cone-shaped finger*

| Structure & Faisceau | $\mu_O$ [cm$^{-1}$] | $\mu_B$ [cm$^{-1}$] | $\sigma_B$ | CNR   |
| -------------------- | ------------------- | ------------------- | ---------- | ----- |
| Faible - conique     | 0.2837 $\pm$ 0.0247 | 0.1342              | 0.1164     | 1.284 |
| Fort - conique       | 0.9571 $\pm$ 0.1161 | 0.1342              | 0.1164     | 7.070 |
| Faible - éventail    | 0.3343 $\pm$ 0.0562 | 0.0073              | 0.0150     | 21.80 |
| Fort - éventail      | 1.8006 $\pm$ 0.3094 | 0.0073              | 0.0150     | 119.6 |

> La pointe des cônes reste observable en vue MPR avec un level du cône fort et fenêtre élevée. 

- ATTN: il faut faire un nouveau scan de référence quand on change le diaphragme. 

Ajouter un bruit artificiel, et recalculer les CNR en fonction du bruit.

- Faisceau conique

*Cône de faible intensité*

| Bruit | $\mu_O$ [cm$^{-1}$] | $\mu_B$ [cm$^{-1}$] | $\sigma_B$ | CNR  |
| ----- | ------------------- | ------------------- | ---------- | ---- |
| 1     | 0.2784 $\pm$ 0.039  | 0.0603              | 0.0864     |      |
| 2     | 0.2755 $\pm$ 0.078  | 0.0513              | 0.0864     |      |
| 3     | 0.2871 $\pm$ 0.1444 | 0.1225              | 0.1537     |      |
| 6     | 0.3739 $\pm$ 0.3211 | 0.1888              | 0.2583     |      |
| 10    | 0.5072 $\pm$ 0.4473 | 0.2673              | 0.3699     |      |
| 20    | 0.7332 $\pm$ 0.6128 | 0.3434              | 0.4890     |      |

*Cône de haute intensité*

| Bruit | $\mu_O$ [m$^{-1}$]  | $\mu_B$ [m$^{-1}$] | $\sigma_B$ | CNR  |
| ----- | ------------------- | ------------------ | ---------- | ---- |
| 1     | 1.0244 $\pm$ 0.1594 | 0.0603             | 0.0864     |      |
| 2     | 1.1315 $\pm$ 0.2268 | 0.0513             | 0.0864     |      |
| 3     | 1.3723 $\pm$ 0.3752 | 0.1225             | 0.1537     |      |
| 6     | 1.9727 $\pm$ 0.6856 | 0.1888             | 0.2583     |      |
| 10    | 2.1643 $\pm$ 0.8002 | 0.2673             | 0.3699     |      |
| 20    | 2.0197 $\pm$ 0.9259 | 0.3434             | 0.4890     |      |

##### Partie 4 - Résolution spatiale et MTF

Calculer la fonction de transfert de modulation MTF(f) du DeskCAT à l'aide de l'équation 3 sur une image 2D ainsi qu'une reconstruction 3D du fantôme *Bar Pattern*. Refaire ces mesures pour les différentes résolutions spatiales possibles ainsi que pour un faisceau en éventail de 1cm. 

![image-20200215232600762](C:\Users\MonteaCristo\AppData\Roaming\Typora\typora-user-images\image-20200215232600762.png)

> Changement de DeskCAT

- Référence à l'air
- On ajoute le fantôme de *Bar Pattern*
- D'abord simple line profile enregistré
- Scan de référence aux changements sur le nombre de projections

- Noter la modulation maximale du système MTF(0)

*Faisceau conique*

| Taille [mm] | f [lp/mm] | Proj. 2D    | CT 1*       | CT 2        | CT 3 |
| ----------- | --------- | ----------- | ----------- | ----------- | ---- |
| 2.0         | 0.5       | 40896/8160  | 2.871/0.131 | 2.489/0.339 | -    |
| 1.5         | 0.67      | 43552/9643  | 3.141/0.601 | 2.068/0.873 | -    |
| 1.0         | 1.0       | 42048/11221 | 2.069/0.927 | 1.512/1.311 | -    |
| 0.75        | 1.3       | 33984/15040 | 1.729/0.844 | -           | -    |
| 0.5         | 2         | 26656/16341 | -           | -           | -    |
| 0.25        | 4         | -           | -           | -           | -    |

| Taille [mm] | f [lp/mm] | CT NF       | CT R1       | CT R2       |
| ----------- | --------- | ----------- | ----------- | ----------- |
| 2.0         | 0.5       | 9.640/1.494 | 5.923/0.102 | 4.167/0.112 |
| 1.5         | 0.67      | 7.563/2.816 | 4.829/0.770 | 2.135/0.531 |
| 1.0         | 1.0       | 6.050/3.417 | 2.923/0.998 | 1.651/0.678 |
| 0.75        | 1.3       | 5.446/3.324 | 3.092/1.673 | 1.893/1.079 |
| 0.5         | 2         | 4.993/4.800 | 2.623/2.071 | -           |
| 0.25        | 4         | -           | -           | -           |

> \* MTF pour différentes résolutions des voxels en mm. 
>
> 0.25, 0.5, 2.0 mm (1, 2, 3) et NF=No filter, R=Ramlack (40 et 160 projections)
>
> \* Les données marquées d'un "-" sont des mesures non résolues.

*Faisceau éventail*

| Taille [mm] | Fréquence [lp/mm] | Proj. 2D    | CT          |
| ----------- | ----------------- | ----------- | ----------- |
| 2.0         | 0.5               | 40512/6048  | 5.508/1.506 |
| 1.5         | 0.67              | 40672/7147  | 4.425/1.840 |
| 1.0         | 1.0               | 37408/8683  | 4.326/2.495 |
| 0.75        | 1.3               | 35776/10624 | 4.008/3.000 |
| 0.5         | 2                 | 28512/12459 | -           |
| 0.25        | 4                 | -           | -           |

##### Partie 5 - ERF, PSF et MTF

Mesurer la fonction de réponse à un rebord (ERF) en prenant une acquisition du fantôme *Step edge*. Enregistrer les profils de ligne sur une projection 2D ainsi que sur la reconstruction 3D dans des fichiers CSV et refaire les mêmes mesures sur images CT avec le faisceau conique pour les configurations présentées au tableau 1. Refaire les mesures avec le faisceau en éventail de 0.5cm et 2cm avec des voxels de 0.25mm.

![image-20200216000024743](C:\Users\MonteaCristo\AppData\Roaming\Typora\typora-user-images\image-20200216000024743.png)

La fréquence spatiale maximale sera déterminée en prenant la transformée de fourier de la dérivée de la réponse ERF(x)  et en notant la fréquence qui fait chuter l'intensité à 10%. 

- On remet l'eau dans le DeskCAT et calibre avec le blank silicon. 
- Scan sur le fantôme de step edge

- Profils de lignes en mode radio enregistrés sur CSV à 3 hauteurs différentes. 
- La même analyse est faite sur les reconstruction CT présentées au tableau 1 et enregistré sur ordinateur. 



### Préparation au rapport

Ludo: parties 4 et 5 

- Erreurs de 2$\sigma$ sur les atténuations.

##### Partie 1

-  2 figures: mu3D et 2D vert et rouge en fonction de l'opacité // mu3D vert en fonction de mu3D rouge
- \* erreurs sur la solution

##### Partie 2

- 1 figure mu en fonction du diaphragme pour 4 structures (4 lignes)

##### Partie 3

- Propagation d'erreur sur le CNR
- 1 Figure du CNR en fonction du bruit pour les deux cônes
- Probablement ignorer les résultats pour l'éventail

##### Partie 4 **

- Figure MTF(f) pour radio, CT 0.25 et CT 0.5 (CT 2.0 est trop flou)  (+ ?) éventail radio et CT 0.25 (+ ?) sans filtre
- \+ effet projections à discuter

##### Partie 5 **

- 2 figures : MTF(f) pour différentes projections et différentes résolutions (peut-être juste limite en fréquence pour alléger)
- 1 figure de la limite supérieure (fréquence pour chute à 10% des MTF) en fonction de la position pour les 5 séries de données (possiblement normalisées)

- Faire des liens avec la partie 4 dans la discussion ou bien dans les graphiques