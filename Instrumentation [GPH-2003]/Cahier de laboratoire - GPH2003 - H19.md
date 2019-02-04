# Cahier de laboratoire - GPH2003 

[TOC]



## LABVIEW

### Préparation

- Langage de programmation **G** .
- Interpolation utilisée entre les données échantillonnées: *Polynomiale* & *Trigonométrique*
- Théorème de Nyquist indique que la fréquence échantillonnage doit être au moins 2 fois plus grande que la fréquence du signal mesuré.

#### But: Reconstruire un signal périodique avec LabVIEW & Nyquist

1.2.1 - Acquisition basique d'un signal

1. Générer une fréquence de 100Hz, amplitude 5V.
2. Brancher *NIDAQ > USB* & *Signal > AI0*.
3. Ouvrir un *VI* et suivre infos dans le protocole pour prendre la mesure.
4. La figure 1.2 montre comment créer un tableau avec des valeurs de temps. Premièrement le tableau est créé, ensuite, il est rempli, puis les valeurs sont divisées par la fréquence d'échantillonnage.
5. Tracer les graphiques

1.2.2 - Paramétrisation

1.2.3 - Reconstruction

1.2.4 - Effet de la fréquence

#### Stratégie du laboratoire:

1. Comprendre comment faire une acquisition sous labVIEW et paramétriser une interface.
2. Reconstruire le signal dans un graphique. Vérifier les différentes stratégies d'interpolation de données. Comparer et utiliser celle qui semble la meilleure pour de données périodiques.
3. Prendre différentes acquisitions de données à différentes fréquences, *sous*, *sur* et *au-dessus* de la fréquence de Nyquist de 2.5*Hz* afin d'étudier l'effet de différentes fréquences échantillonnage.
4. Comparer les résultats avec les deux types d'interpolation et discuter des résultats.



### Séance

Le labVIEW est débuté. Familiarisation grossière avec LabVIEW:

- Clic droit dans le diagramme permet de choisir différentes fonctions afin de faire notre instrument virtuel. 
- La construction de tableau se fait en 2 étapes. On doit initialiser le tableau, puis le remplir à l'aide d'une *Boucle* et de la fonction *Remplacer élément*.
- Entrée d'un tableau dans une boucle doit passer dans un registre à décalage.

La création du VI a été faite selon le protocole:

![VI_param](assets/VI_param.PNG)

Un échantillonnage sans entrée a été effectué afin d'observer les variations d'incrémentation du signal du bruit. On voit que les valeurs oscillent à coups de *0.002467+0.000087=.* Cette incrémentation  montre effectivement la résolution pour un VI programmé sur une plage de -5 à 5V. Ainsi, sachant que la carte est programmée sur 12 bits, on pourrait trouver la résolution numérique du signal mesuré en faisant $\frac{10}{4096}=0.00244​$ V



Ensuite, un échantillonnage du signal sinusoidal a été effectué. 
**Paramètres du sinus:** F = 100Hz, CC = 10V
**Paramètres du VI:** Fréquence d'échantillonnage = 1000Hz, Nombre de mesures = 100, Plage = [-5,5], Résolution = 0.00244

Image de la capture Test:

![VI_param_faceavant](assets/VI_param_faceavant.PNG)

Afin d'effectuer des mesures et de faire de l'interpolation trigonométrique et polynomiale, un Nouveau VI a été construit afin d'avoir ces nouvelles fonctions:

![VI_interpol](assets/VI_interpol.PNG)

#### Acquisition des données

Tableaux des fichiers utilisés

Les valeurs constantes sont N=10, F=100 et Résolution Interpolation=1000

**Dans les fichiers:**

Colonne 1 = temps absolu
Colonne 2 = temps de mesure
Colonne 3 = Tension
Colonne 4 = polynomial
Colonne 5 = Fourier

| Description           | Fréquence [Hz] |
| --------------------- | -------------- |
| Mesure test du sinus  | 1000           |
| nyquist_data_1000.csv | 1000           |
| nyquist_data_750.csv  | 750            |
| nyquist_data_500.csv  | 500            |
| nyquist_data_400.csv  | 400            |
| nyquist_data_300.csv  | 300            |
| nyquist_data_200.csv  | 200            |
| nyquist_data_100.csv  | 100            |
| nyquist_data_90.csv   | 90             |
| nyquist_data_60.csv   | 60             |
| nyquist_data_30.csv   | 30             |
| nyquist_data_20.csv   | 20             |
| LOGICIEL PLANTE       | 5              |
| LOGICIEL PLANTE       | 2              |



## Capteur de Courant

### Préparation

#### Les caractéristiques majeures d'un capteur sont souvent

- Étendue (plage) sur laquelle la mesure est valable
- Linéarité du capteur. Est-ce que la réponse du capteur est directement proportionnelle au signal physique mesuré?
- Réponse fréquentielle (rapidité de la réactivité du capteur)
- Résolution (plus petite variation mesurable)
- Sensibilité (gain du capteur, petite variation physique=grande variation signal)

#### Types de capteurs de courant

- Shunt: Résistance connue parcourue par un courant et mesure à ses bornes. Résistance faible pour ne pas influencer la mesure, $\Delta V$ détectable, tolérance élevée.
- Hall: Le champ magnétique produit par le passage du courant dans un fil fait dévier la trajectoire d'électrons et créé une différence de potentiel aux bornes du capteur à cause de cette variation de densité électronique de par et d'autre du capteur. Une gaine coaxiale ne permet pas une mesure par effet hall (faraday effet)

#### Manipulations

##### Shunt

1. Faire le circuit du protocole. Calculer la valeur nécessaire de la résistance ainsi que sa tolérance en puissance
2. Faire varier la tension source jusqu'aux limites de la source/tolérance avec des incréments faibles afin d'avoir une bonne résolution.
3. Mesurer la résistance totale du circuit avec précision et trouvez le courant en fonction de la tension.
4. Comparer la méthode au point 2 et 4



### Séance

#### Shunt

0.05V = 0.14A

$R_{shunt}=(0.01\pm0.25\%)\Omega$ résistance réelle , $P_{max}=(5\pm )W$
$R_{circuit}=(2.3\pm0.5)\Omega$

MAX amperage circuit = 1.4A, donc on se limite à 1A



| Tension source [V$\pm$0.0] | Tension $R_{shunt}$ [mV$\pm$0.002] | Courant dans $R_{shunt}$ [mA$\pm$0] | Courant total [mA$\pm$0] | COurant sur la source [A] |
| -------------------------- | ---------------------------------- | ----------------------------------- | ------------------------ | ------------------------- |
| 0.05                       | 0.194                              | 0                                   | 0                        | 0.02                      |
| 0.1                        | 0.415                              | 0                                   | 0                        | 0.04                      |
| 0.15                       | 0.633                              | 0                                   | 0                        | 0.06                      |
| .20                        | 0.854                              |                                     |                          | 0.09                      |
| .25                        | 1.074                              |                                     |                          | 0.11                      |
| .3                         | 1.298                              |                                     |                          | 0.13                      |
| .35                        | 1.519                              |                                     |                          | 0.15                      |
| .4                         | 1.738                              |                                     |                          | 0.17                      |
| .45                        | 1.958                              |                                     |                          | 0.2                       |
| .50                        | 2.172                              |                                     |                          | .22                       |
| .60                        | 2.614                              |                                     |                          | 0.26                      |
| .70                        | 3.053                              |                                     |                          | 0.31                      |
| .80                        | 3.488                              |                                     |                          | 0.35                      |
| .90                        | 3.924                              |                                     |                          | 0.39                      |
| 1.00                       | 4.357                              |                                     |                          | 0.44                      |
| 1.1                        | 4.794                              |                                     |                          | 0.48                      |
| 1.2                        | 5.225                              |                                     |                          | 0.52                      |
| 1.3                        | 5.699                              |                                     |                          | 0.57                      |
| 1.4                        | 6.128                              |                                     |                          | 0.61                      |
| 1.5                        | 6.508                              |                                     |                          | 0.65                      |
| 1.6                        | 6.992                              |                                     |                          | 0.7                       |
| 1.7                        | 7.409                              |                                     |                          | 0.74                      |
| 1.8                        | 7.830                              |                                     |                          | 0.78                      |
| 1.9                        | 8.246                              |                                     |                          | 0.83                      |
| 2.0                        | 8.660                              |                                     |                          | 0.87                      |
| 2.2                        | 9.400 $\pm0.05$                    |                                     |                          | 0.94                      |
| 2.4                        | 10.190 $\pm 0.1$                   |                                     |                          | 1.02                      |
| 2.6                        | 10.985$\pm 0.1$                    |                                     |                          | 1.10                      |

Graphique du calcul des courants selon la tension de la source.



Comparaison du courant calculé à partir de Rtotal et Rshunt:

> 



#### Hall

Construire circuit d'alimentation pour alimenter capteur Hall.

1. Monter le circuit à 4.3
2. Choisir un résistance R (Rtotal remesuré avec les connections =2.87+-0.05 )
3. Garder les mêmes résistances sur le circuit de shunt et mettre de la sur le capteur à effet hall. Prendre les mesures en incrémentant la tension de la même manière qu'avec le shunt afin de tracer la courbe d'étalonnage. le courant passant dans le capteur est de 16.990mA +- 0.1

OFFSET 6.4527

| Tension Source [V$\pm$0.05] | Tension de Hall [V$\pm$0] | Courant source |
| --------------------------- | ------------------------- | -------------- |
| 0.1                         | 6.4510                    | 0.04           |
|                             | 6.423                     | 0.07           |
| 0.3                         | 6.4472                    |                |
|                             |                           |                |
| 0.5                         | 6.4436                    | 0.18           |
|                             |                           |                |
| 0.7                         | 6.4400                    | 0.25           |
|                             |                           |                |
| 0.9                         | 6.4360                    | .32            |
|                             |                           |                |
| 1.1                         | 6.4323                    | .4             |
|                             |                           |                |
| 1.3                         | 6.4288                    | .47            |
| 1.4                         |                           |                |
| 1.5                         | 6.4251                    | .54            |
| 1.6                         |                           |                |
| 1.7                         | 6.4216                    | .61            |
| 1.8                         |                           |                |
| 1.9                         | 6.4179                    | .68            |
| 2.0                         | 6.4167                    | .71            |
| 2.1                         |                           |                |
| 2.2                         | 6.4127                    | .78            |
| 2.3                         |                           |                |
| 2.4                         | 6.4094                    | .84            |
| 2.6                         | 6.4063                    | .91            |

des grandes variations avaient étés observée à cause des vibrations sur la table. Celles-ci jouaient probablement sur les contacts des connections, augmentant ainsi la résistance du circuit. Cela a essayé d'être minimisé. 

Puissance dissipé pour le capteur à effet hall:

Alimentation de l'ampliOP 15V*0.01A + Alimentation du capteur 6.00V*0.03A

=0.3 W constant sur toute la plage



##### Graphique de la courbe d'étalonnage 





##### L'angle influence-t-il la mesure?

De combien approximativement?
Angle vs Tension

Le courant du circuit a été setté à 1A constant (2.86V) au borne du circuit.

à 90, 6.406

à 45 6.39

à 60 6.29

Ça diminue pcq la projection perpendiculaire est plus petite que quand il est à 90, soit totalement perpendiculaire

##### Le courant d'alimentation du capteur influence-t-il les mesure?

Oui, le courant étant augmenté, le champ magnétique est plus intense. Un champ magnétique plus grand traversant un courant similaire engendrera un un déplacement des électrons plus grand à cause de la force de Lorentz plus élevée et donc une tension plus grande.

Une augmentation de 0.2V génère environ la même variation de tension aux bornes du capteur.



Mesure de la variation en fréquence
Capteur HALL

un générateur de fréquence a été envoyé dans le fil parcourant le capteur a effet Hall. Cette fréquence a été augmentée jusqu'à ce que le signal du capteur commence à varier étrangement.

Fréquence de coupure = 12kHz

Capteur SHUNT

même chose fréquence de coupure =30kHz



#### Comparaison des caractéristiques des capteurs

| Caractéristique   | Capteur Shunt | Capteur Hall |
| ----------------- | ------------- | ------------ |
| Plage             | [0-1]         | [0-1]        |
| Sensibilité[mV/A] | -             | +            |
| Linéarité         |               |              |
| Résolution        |               |              |
| Comsommation      |               | 0.3W         |
| Bande passante    |               |              |
| Synthèse          |               |              |

Quel capteur est meilleur? Dans quelles situations l'un est-il plus avantageux que l'autre?





## Capteur de Position Linéaire

### Préparation

### Séance



## Conditionnement

### Préparation

### Séance



## Capteur de Température

### Préparation

### Séance



## Capteur de Position Angulaire

### Préparation

### Séance



## Débitmètre

### Préparation

### Séance



## Capteur de Pression

### Préparation

### Séance



## Jauge de déformation

### Préparation

### Séance