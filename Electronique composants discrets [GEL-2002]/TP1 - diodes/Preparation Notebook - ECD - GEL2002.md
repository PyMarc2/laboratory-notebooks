# LAB1 - Diodes

###  1.Preparation

1.1- Paramètres de la diode 1N4148 [Datasheet](1N914-1N4148.pdf)

- V~F~ = 1.0V @ 10mA
- I~R~ = 25nA @ 20V

1.4 - Simulation Altium

![1548127393013](assets/1548127393013.png)

![1548127586470](assets/1548127586470.png)

À partir de la courbe générée en simulation, on peut retrouver un $R_d=\frac{\Delta{V}}{\Delta{I}}=16.6\Omega$ 

On remarque qu'altium utilise le modèle exponentiel.

Il s'agira de mesurer la variation de la courbe *iv* en fonction de la température. Un thermomètre variable programmable sera utilisé avec un arduino. [Datasheet thermomèetre](DS18B20.pdf)



### Experience au laboratoire

#### 2. Diodes à jonction PN

**2.1 - Courbe i-v**

![img](assets/51588892_786302388397597_8728142009610534912_n.png)

![img](assets/51157291_404897230268983_4006787209620357120_n.png)

**2.2 - Coefficient n**

$$n=\frac{V_2-V_1}{V_T\ln[I_2/I_1]} = \frac{0.800-0.754}{0.0257\cdot\ln(36/16)}\approx2.3$$

La valeur calculée correspond approximativement à la valeur théorique des diodes discrètes qui est de 2.



**2.3 - Courant de fuite**

Le courant de fuite mesuré à $-20.0V​$ est de $7nA​$. Cela est conforme à la fiche technique de la diode qui assure un courant de fuite $<25nA​$.



**2.4 - Comparaisons**

*Simulation:*

- $R_d=\frac{\Delta V}{\Delta I}=\frac{1-0.75}{0.02-0.007}=19.9.​$

*Expérience:*

- $R_d=\frac{0.8-0.754}{0.036-0.016} \approx 3.3$
- $n\approx 2.3$

*Datasheet:*

- $R_d \approx 1.8​$
- $n\approx 2​$

Les valeurs expérimentales semblent se rapprocher bien plus des valeurs de la datasheet que des valeur calculées à partir de la simulation. Peut-être que le modèle de simulation sélectionné n'était pas le bon ou que la simulation a été effectuée avec les mauvais paramètres. Parmis les modèles utilisés pour modéliser le comportement d'une diode, il y a le modèle idéal, le modèle linéaire et le modèle exponentiel.

- Modèle idéal: (+) Très simple, rapide; (-) Faux, pas utilisable en pratique
- Modèle linéaire: (+) Approximatif, rapide, simple; (-) Ne tient pas en compte la zone de transition entre le blocage et la zone d'opération linéaire
- Modèle exponentiel: (+) Modélisation juste; (-) Plus complexe que les autres modèles



#### 3. Effets de la température sur la diode à jonction PN

Le circuit suivant a été effectué:

![1549167492701](assets/1549167492701.png)

Le potentiomètre a été ajusté afin d'obtenir $i_D=50mA$
La diode a ensuite été refroidie. Le courant de 50mA a été maintenu afin d'observer le décalage de voltage au borne de la diode en fonction de la température. Un décalage d'environ $-2mV/^\circ C$ a été observé, comme présenté sur le graphique ci-dessous. Cette valeur est également ce qui est présenté dans la datasheet de la diode 1N4148 à la Figure 6.

 

![img](assets/51168112_237751813839784_3023057360294772736_n-1549170882915.png)



![img](assets/51177147_389096781840504_1830302417724375040_n.png)

#### 4.Diode Schottky et le redressement

**4.1 - iv Schottky **
Le circuit suivant a été réalisé

![1549169164539](assets/1549169164539.png)

**4.1 -** Les mesures suivantes ont été prises:

![img](assets/51047869_2281745781870309_7005018812835692544_n.png)

On remarque une hystérésis dans la courbe i-v de la diode. Celle-ci est probablement dû au décalage de la courbe i-v de la diode en fonction de la température. L'augmentation de température est causée par le passage du courant dans la diode.



**4.2 - Courant de fuite**
Le courant de fuite mesuré à -20.0V aux bornes de la diode est de 5.9uA.



**4.3 - Diode 1N5817**

- $r_d = $ $\frac{\Delta V}{\Delta I}=\frac{0.078}{0.0186}=4.19\Omega$
- $V_{th} \approx 200mV $, environ comme l'indique la fiche technique.



![img](assets/51138341_1922739647835639_4115455448486772736_n.png)

![TEK0000](assets/TEK0000.JPG)

*Rectification simple d'un signal sinusoïdal à l'aide d'une diode et d'une résistance de 300kOhms.*

![TEK0001](assets/TEK0001.JPG)

*Rectification simple d'un signal sinusoïdal à l'aide d'une diode et d'une résistance de 100Ohms.*



On observe ici que le redressement dépend de la vitesse de décharge du condensateur qui dépend de la constante RC.

La diode du circuit a été remplacée par une diode 1N5817 afin de vérifier l'impact sur la rectification. 





![TEK0005](assets/TEK0005.JPG)

*Rectification simple d'un signal sinusoïdal à l'aide d'une diode et d'une résistance de 300kOhms avec une diode 1n5817.*

![TEK0004](assets/TEK0004-1549172932963.JPG)

*Rectification simple d'un signal sinusoïdal à l'aide d'une diode et d'une résistance de 100Ohms avec une diode 1n5817.*



On remarque que la rectification n'a pas été améliorée par l'augmentation de la résistance. Il est possible qu'une erreur dans le circuit ait causé ces mauvais résultats. On remarque même que le signal source est influencé par le circuit.



On peut discuter de l'utilisation d'une diode schottky pour le redressement. La Schottky possède une tension seuil plus basse, ce qui permet de dissiper moins de puissance en pertes calorifiques. Également, le temps de réponse des diodes schottky est largement supérieur, cela peut être utile pour une source alternative rapide. Le désavantage de la Schottky est son courant de fuite en polarisation inverse qui est de l'ordre des uA, ce qui est plus important que les diodes normales.



#### 5.Diode Zener

**5.1 -  courbe i-v**

Le montage suivant a été réalisé:

![1549173538168](assets/1549173538168.png)

La courbe i-v suivante a été mesurée sur l'oscilloscope:

![img](assets/51545834_355098805327616_7316873390311079936_n.png)

La courbe observée est fidèle aux indications de la fiche technique de la diode 1N4733A. La tension de seuil correspond environ au 1.2V indiqué et la tension de zener à -5V environ.



#### 6. Protection

La charge inductive permet d'emmagasiner de l'énergie sous forme de champ magnétique. La tension à ses bornes est déterminée par l'équation $dV = L\frac{dI}{dt}$. Ainsi, couper la source de courant induit un $\frac{dI}{dt}$ élevé qui engendre donc une tension très élevée aux bornes de la bobine. Cette tension peut engendrer des courts-circuits.



Le circuit suivant a été réalisé:

![1549174819694](assets/1549174819694.png)

La mesure des pics de tension aux bornes de la bobine ont révélé une tension maximale d'environ 118V.

![img](assets/51032893_232647177645385_3050908161625030656_n-1549174911877.png)



On observe les pics de tensions mesurés avec diode de protection. Il s'agit d'un grossissement des pics de tension. On remarque que la tension maximale est beaucoup moins importante que le 118V mesuré sans protection.

![TEK0008](assets/TEK0008.JPG)



Une augmentation de la fréquence de commutation diminue l'amplitude des pics de tension aux bornes de l'inductance en raison du temps de réponse intrinsèque de l'inductance. De plus, on peut ajouter une résistance en série avec la diode, afin de limiter les retours de courants importants. Une diode seule peut laisser passer d'importants courants.



#### 7. Détection de l'intensité lumineuse

Le montage suivant a été réalisé:

![1549175454002](assets/1549175454002.png)

La résistance Rf=300kOhms



**7.2 - Courant de la photodiode**

Le courant traversant la photodiode pour différents degrés d'exposition lumineuse a été mesuré. Les résultats sont présentés dans le tableau suivant:

![img](assets/51210429_324904841479577_1621710068204437504_n.png)

On remarque que le courant de la photodiode n'est pas nul lorsque celle-ci est couverte. On appelle cela le *Dark current*.

**7.3**

Le courant traversant la photodiode engendre un différence de potentiel à l'entrée de l'ampliop, ce qui se traduit par une augmentation de la tension de sortie. L'utilisation d'une résistance Rf élevée permet d'avoir un gain élevé, ce qui permet d'augmenter la différence de potentiel pour une même variation de tension à la photodiode.



**7.4 / 7.5**

Les mesures du PWM avec et sans filtre RC sont présentées dans le tableau ci-dessus.



Variation du Duty-cycle (sans filtre RC)

![TEK0010](assets/TEK0010.JPG)

*PWM mesuré lorsque la photodiode est couverte*

![TEK0011](assets/TEK0011.JPG)

*PWM mesuré lorsque la photodiode est à la lumière ambiante*

![TEK0012](assets/TEK0012.JPG)

*PWM mesuré lorsque la photodiode est près d'une source lumineuse intense.*



Les mesures suivantes ont étés effectuées avec un filtre RC. On remarque que la composante alternative du signal n'est plus présente et que seulement une tension moyenne est mesurée.

![TEK0013](assets/TEK0013.JPG)

*Signal de sortie filtré lorsque la photodiode est couverte*

![TEK0014](assets/TEK0014.JPG)

*Signal de sortie filtré lorsque la photodiode est à la lumière ambiante*

![TEK0015](assets/TEK0015.JPG)

*Signal de sortie filtré lorsque la photodiode est près d'une source lumineuse intense.*



**7.6**

Les mesures des tensions de seuil des DELs sont dans le tableau plus haut.



**7.7**

Le montage suivant a été réalisé:

![1549176640000](assets/1549176640000.png)

Il est nécessaire d'utiliser un tampon dans le circuit afin de limiter le courant traversant les DEL. Cela permet d'avoir l'intensité lumineuse voulue.



**7.8**

La mesure des tensions de seuil des DELs ont été mesurées et sont présentées dans le tableau plus haut.

1. Oui, les résultats concordent avec les tensions de seuil mesurées en 7.6.
2. Il y aurait diminution de l'intensité lumineuse des DELs.