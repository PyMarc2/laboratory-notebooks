# Laboratory Notebook - TPOB GPH4102

[TOC]



## Raman Spectroscopy

### Preparation

#### Theory

Raman effect: re-emission of radiation from an exited state of a sample. [raman spectroscopy](https://en.wikipedia.org/wiki/Raman_spectroscopy)

Rayleigh scattering: re-emission at same wavelength

Stokes: loss of energy in vibrational states excitation of the sample, re-emission has a bigger wavelength

Anti-Stokes: synchronous phonon (vibrations) gives a virtual higher state of energy, re-emission has smaller wavelength

Vibration of certain molecules or molecule bonds are relative the the bond. Thus, the absorption in the vibrational states will be different for different bonds. It is possible to characterize a material looking at its bonds.

Raman scattering is really weak. It is important to reduce/minimize instrumentation noise and other sources like thermal, external photons, etc.

#### To do before starting

1. Download LightSpec software (should be with the camera)



#### Necessary information

1. **Mercury Spectrum for CCD calibration**

   [Data of Hg spectrum](http://njsas.org/projects/atoms/spectral_lines/1/mercury_nist.html)

   Important peaks for calibration will be between 633nm and lower (around 800nm since a $$\Delta\lambda=230$$ is rare) since we excite our sample with a 633nm laser. According to [this site](https://en.wikipedia.org/wiki/Coherent_anti-Stokes_Raman_spectroscopy), Stoke's shift is much higher than anti-stokes, since anti-stokes requires the superposition of a photon while the electron is in a virtual state. Stoke's shift occurs more naturally, since the excitation will lead to an eigen energy value. 

   *Interesting peaks with high relative intensity:* 404.656nm(1800), 435.833nm(4000), 546.074nm(1100), 614.950nm(1000), 690.752(250), 708.190(250).

   The spectrum on the CCD should start at around 630nm, so it will be calibrated with the 546nm and 614nm peaks, which will be highly distinguishable.

2. **Pixis 100 CCD**

   [Explication théorique](https://www.ptgrey.com/white-paper/id/10912)

   [Pixis100 Datasheet](https://www.princetoninstruments.com/userfiles/files/assetLibrary/Datasheets/Princeton_Instruments_PIXIS_100_rev_5_1_10_22_14.pdf)

   The CCD has 2 modes:

   - High well sensitivity : Well depth of *300 ke- (typical), 250 ke- (min)*

   - High well capacity : Well Depth of *1 Me- (typical), 750 ke- (min)*

   The probability that a photon excites an electron is a function of the spectrum. A python code here makes the necessary corrections on data taken with the PIXIS100-B CCD. 

   | [img](https://github.com/SebJercz/TPOB/raw/master/home/sebastien/Desktop/git/fig/raman/absorption.gif) |
   | :----------------------------------------------------------: |
   |         Figure - Quantum efficiency of the 100PIXIX          |

   ```python
   # Code to correct the measurments of the CCD-PIXIS100-B
   ```

   The number of photons necessary to increment a pixel by 1 will depend on the mode selected. A higher capacity will require a higher number of electrons. The camera captor is coded in 16 bits: 65535 values. Thus, if we use the typical values:

   - High well sensitivity : $\frac{300000}{65535}\approx 4.57771$ /electron per pixel incrementation.

   - High well capacity :  $\frac{1000000}{65535}\approx 15.25902$ /electron per pixel incrementation.

   [QE graph linear approximation](https://github.com/SebJercz/TPOB/blob/master/fig/raman/Screenshot%20at%202018-09-24%2013_24_29.png)

3. **Static Photon Noise / Noise Relative to Measure**

   The Datasheet specifies static noise. No measure-dependent noise seems to be in effect here.

   For the PIXIS 100-B, there are 2 acquisition speed, which affect the noise:

   - 100kHz: 3e- rms (typical), 5e- rms (max)
   - 2 MHz: 11e- rms (typical), 16e- rms (max)

   Assuming the noise is a varying *sinusoidal* signal. The peak noise will rather be $$\sqrt{2}\cdot U_{rms}$$

   The **noise relative to the measure** @-80$^{\circ}C$ is typically 0.001 electron/photon/second

   It doesn't mention a dependency to acquisition speed/mode. So the measurement noise is given by this relation:

   [Graph of relation](https://github.com/PyMarc2/Laboratory-Notebook/blob/master/raman_spectroscopy/noisevsphotons.png)


4. **Vibration Frequency**

   Here is a [list]() of the usual bonds with emission wavelength associated

   The Raman wavelength is obtained by: $v =  \frac{1}{632.8nm} - \frac{1}{\lambda (x)}$ . With $$\lambda (x) =  700\text{nm}$$, it gives $$151 7.07$$ cm$$^{-1}$$.

   With this [table](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=1008896699),  it is possible to predict the emission wavelength of different molecules, as these tables reveal the emission of specific bonds. The values where taken from [this table](https://www.utsc.utoronto.ca/%7Etraceslab/raman%20correlation%20table.pdf), [this document](http://faculty.sites.uci.edu/chem2l/files/2011/03/RDGVibrationalSpec.pdf)


5. **Noise Evolution With Time Integration**

   Here is a [table](https://docs.google.com/spreadsheets/d/1T_n07VUFYqAoMUErGHkXlpteVMmAV6pEA5eiwz1RgZs/edit#gid=1891590538) ready for the Time/Noise measurements.

6. **Chlorophyll Spectrum**

   [Values taken on this site](http://www.photosynthesis.ch/fluorescence.htm)

   Absorption peaks : 430nm and 662nm

   Emission peaks : 669nm



7. **Olive Oil**

   Chemical compound of Olive Oil is a triglyceride with 3 fatty-acids.

   $C_{55}H_{98}O_6$ is an example of chemical formula for a fat.

   Olive Oil Fatty-acids are unsaturated. There should be presence of C=C bonds.

   Also, in the glycerol, C-C, C-O, C=O, C-H, bonds will also be present.

   This  gives the expected range of emission of these bond

- 13.8% saturated (C-C)
- 70% mono-unsaturated (C=C)
- 13.2% poly-unsaturated (many C=C)



### In Lab

#### Discussion with Simon Rainville

1. Difference between fluorescence and Raman scattering

   Fluorescence is the excitation of an electron at a specific energy level, which then leads to the energy loss in complex non-radiative processes. Fluorescence excitation happens only at specific wavelengths.

   Raman scattering has the same output: a bigger wavelength, thus a lower energy photon. The difference is in the excitation processes. The electron doesn't have to be excited at a specific level. It will rather be excited at a virtual level, and then release its virtual energy into vibrational modes of certain electron bonds. These energy variations vary according to the bond excited.

2. Three types of noise
   - **Measure noise:** the action of measuring generates noise in the process. It is constant a each measure.
   - **Thermal noise:** There is a probability that (because of the Boltzmann distribution of energy) it is possible that an electron will be excited. That probability is a function of time. So for example, There is 0.005% of chance that an electron is excitedper second because the thermal energy at -80celcius. (not exact numbers)
   - **Schottky noise**: Physical phenomenon's are usually described by Poisson's distribution. It is the case for photon emission of a sample. It is possible that the number of photon emitted are not totally the same for two measures. For Poisson's distribution, The standard deviation of the emission of a photon is the square root of number of photons detected. Thus, because we are interested in the ratio between the average value and the deviation, we shall do the ratio. So the Signal Noise Ratio (SNR) = $$\frac{N}{\sqrt{N}}=\sqrt{n}$

#### Manipulations

##### Setup exploration

Important parts of the setup :

- Notch filter : Blocks the laser emission of 633nm that could come from rayleigh scattering or the laser himself. Important, light collected must arrive normal to the lens.
- Vertical Slit : manages the resolution. a thinner slit means less light, but a thinner bar of light, the goal is to make the slit of light the width of a pixel, so no resolution is lost and the maximum light enters the spectrometer.

##### Software exploration

WINSpec32 is the software to acquire spectrum with the PIXIS100 CCD. Here are the different parameters used during all the experimentation:

- The rate was set to 100K Hz
- The mode is High Capacity
- The gain was 1
- The ASCII output is on
- The accumulation of spectrum will probably vary, but is set to 1, will notice if changed
- The integration time will change 

Picture of the setup dialog box:

To acquire, the Acquire button is used.

##### Readout Noise characterization

In WINSpec32, we asked the software to output a ASCII file. It saves .txt files with (spectrum number, x, y) convention

| Integration time (ms) | Filename  [*.txt]  |
| --------------------- | ------------------ |
| 100                   | bruit_mesure_100ms |
| 75                    | bruit_meusre_75ms  |
| 50                    | bruit_meusre_50ms  |
| 25                    | bruit_meusre_25ms  |
| 10                    | bruit_meusre_10ms  |
| 5                     | bruit_meusre_5ms   |
| 1                     | bruit_meusre_1ms   |
| 0.1                   | bruit_meusre_100us |
| 0.001                 | bruit_meusre_1us   |

The average noise is approximately 600/65535 per pixel.

**INFO** Binning doesn't divide by the number of pixel, it adds. So the limit of the value on the software is 65535*100 = 650k. 

Daniel verified our configuration, He changed the Rate from 100kHz to 2MHz. The Readout noise measures were retaken with that configuration so the name of the files don't change.

##### Thermal noise characterization

Thermal noise should appear on long integration time.

| **Temps d'intégration** (s) | Nom du fichier       |
| --------------------------- | -------------------- |
| 1                           | bruit_thermique_1s   |
| 10                          | bruit_thermique_10s  |
| 50                          | bruit_thermique_50s  |
| 100                         | bruit_thermique_100s |

**Observations : ** We noticed that long exposition increased the noise proportionaly to the integration time. Also, there were weird spikes observable in the files. Even with all the lights off, the spikes are there. Maybe bleeding filter???

##### Photon noise (statistical)

We think that this noise should increased proportionally to sqrt(N)

| **Temps d'intégration** (s) | Nom du fichier          |
| --------------------------- | ----------------------- |
| 0.001                       | bruit_grenaille_1ms     |
| 0.1                         | bruit_grenaille_100ms   |
| 1                           | bruit_grenaille_1s      |
| 5                           | bruit_grenaille_5s      |
| 10                          | bruit_grenaille_10s     |
| ~~50~~                      | ~~bruit_grenaille_50s~~ |

**Observations : **General shape of the spectrum stays the same

gossage avec Daniel :

bruit de mesure 79500

80300 ± 150 pour 30ms

80850 ± 150 pour 60ms

85200 ± pour 240ms

Pour que laugmentation du signal soit linéaire, il faut donc soustraire le bruit de mesure. (et aussi le bruit thermique?) Pour le bruit de photon, on peut également considérer une zone du spectre ou l'intensité est constante (pixel 980 et 1020) pour caractériser la moyenne et l'écart type du signal obtenu afin d'éviter de prendre de tres longues acquisisitons



##### Étalonnage de la caméra sur l’axe des longueurs d’onde

Trois gros pics, creux = Pics seront identifiés avec le tableau de pics du mercure afin de changer l'axe de pixels à un axe en longueur d'onde

On remarque que dans les données il y a un "creux " dans le signal, on détermine que c'est le manque de signal causé par le filtre qui bloque le 632.8nm, alors les longueurs d'ondes a droite de ceux creux sont les longueurs d'onde plus élevées (réseau de diffraction en transmission envoie les plus haute longueurs d'onde plus en angle). Les pics visibles sont donc des pics plus haut que 632nm

##### Entre les deux périodes

Les pics visibles dans le spectre du mercure sont aux valeurs de pixel 589, 844, 1092 et 1106. Selo [le tableau des pics du mercure](http://njsas.org/projects/atoms/spectral_lines/1/mercury_nist.html), il y a des pics du mercure à environ 671, 690, 708 et 709nm. Si on graph ces valeurs, on remarque que que c'est très linéaire, alors les pics ont bien été identifié. On peut faire un polyfit linéaire pour trouver la fonction qui va transformer les valeurs de pixel en longueur d'onde en nm, ce qui donne $\lambda = 0.07343918330732058x + 627.8355813527794$$

[Lien vers spectre mercure](https://github.com/SebJercz/TPOB/blob/master/raman/fig/mercure.png) [Lien vers spectre olive oil](https://github.com/SebJercz/TPOB/blob/master/raman/fig/oliveoil.png)

#### Second period

##### Substances Raman spectrum

| Substance       | Spectrum File             | Integration time[s] | Spectrum accumulation |      |
| --------------- | ------------------------- | ------------------- | --------------------- | ---- |
| Olive oil       | olive_oil.txt             |                     |                       |      |
| Sunflower oil   | sunflower_oil.txt         | 60                  | 5                     |      |
| Peanut Oil      | peanut_oil.txt            | 10                  | 10                    |      |
| Canola Oil      | canola_oil.txt            | 60                  | 10                    |      |
| Corn Oil        | corn_oil.txt              | 60                  | 5                     |      |
| Ethanol         | ethanol.txt               | 50                  | 1                     |      |
| Methanol        | methanol.txt              | 180                 | 1                     |      |
| Isopropanol     | isopropanol.txt           | 120                 | 1                     |      |
| Sucrose         | sucrose.txt.              | 120                 | 3                     |      |
| Glycerol        | glucose.txt               | 120                 | 1                     |      |
| A,B,C,D,E,F,G,H | A.txt, B.txt, C.txt, etc. | 20                  | 1                     |      |

For C accumulation was 3, for D 8, for G 5.

For all these substances, gain was set to 1. Rate was 2MHz. Readout was "Low Noise"

##### Discussion with Daniel and Simon about Fluo/Raman

Daniel explained to us a fundamental thing about measuring Raman spectrum in the presence of fluorescence.  Since the signal of fluorescence is much more important than the Raman signal. However, it is possible to detect the Raman signal in the fluorescence signal. Since our Fluorescence signal is very large , for example the olive oil: the max signal after 100ms of integrating is 12000. The fluorescence signal is very strong. No peaks on the fluorescence signal can be seen. 

If we take a pure sample, let's say ethanol. For 50s of integration, we got a minimum signal of about 2 000 as well. Because we want to see those small peaks

Thus, the signal is approximatively 3000 times weaker. for 100ms the Raman is 4. The statistical noise of the fluorescence is $\sqrt{12000}=110$. We want a Raman signal approx. 5 times bigger than the noise.

$4t[ms]/100=5*\sqrt{12000*t/100}$

isolating $t$, it gives approx.. 30min of integration for a 5 times bigger Raman signal over the noise of the fluorescence. Retaking the spectrum of the olive oil effectively shows some spikes that weren't seen before.



It has been found that the high peaks at about 200pixels  is the filter bleeding. The 4f system before the spectrometer was not aligned, which caused the light of the fluorescence to entre the system at a weird angle. The filter must have collimated light at its input




## Confocal microscopy

### Preparation

Microscope confocal : permet d'uniquement détecter la lumiere qui provient du plan focal à l'aide d'un sténopé, ce qui permet d'observer des échantiollons avec une certaine epaisseur sans avoir de flou. Toutefois, il faut balayer l'échantillon car la plumière est captée par un PMT qui n'imite qu'un seul pixel.

Signal amplifié avec un photomultiplicateur (PMT). Éviter de mettre lumière ambiante directement dans PMT et de ne pas le saturer, toujours commencer avec gain nul.

Fluorescence : molécule absorbe photons a certaine longueur d'onde (spectre d'excitation) et le réemet des photons (spectre d'émission) à des longueurs d'onde plus longues car les photons perdent de l'énergie par vibration (Stokes shift). $\epsilon$ = coefficient molaire, qté de photons absorbés, $\sigma _a$ = section efficace d'absorbtion, $n$ = efficacité quantique

Marqueurs : Molécule endogène, molécules organiques, protéines fluorescentes, points quantiques

Photoblanchiment : durant excitation les molécalues peuvent faire des réaction et perdre leur propriété fluorescente. Eviter les temps d'Acquisition très long.

### In Lab

#### Observations montage

*Explication générale :* 

1. laser --> galvanomètre = Balayage XY.

2. Balayage XY --> un système 4f grossissement 3x. (pour remplir le Back Aperture de l'objectif afin d'avoir la résolution maximale.).

3. Émission de fluorescence --> déscannage

4. Miroir dichroique : laisse passer la lumière jusqu'à une certaine longueur d'onde, puis la réfléchie. 

*Deux problemes* : on travail en réfelctance alors la longueur d'onde ne change pas, le laser devrait être réfléchi autant à l'allé et au retour. De plus, la fluorescence réemet de la lumiere a plus haute longueur d'onde (a moins d'Avoir anti-stokes, ce qui n'est pas le cas), alors le miroir devrait encore bloquer la lumière. Ces deux problèmes sont ngéligeable puisque que le miroir n'est pas parfaitement alligné a 45 degré et qu'il n'est pas parfait, donc il y a toujours environ 1% du signal qui le traverse (SPEC SHEET). Ce 1% de signal est toutefois très suffisant pour que le PMT détecte et amplifier le signal.

PMT :  ??? HAMAMATSU?

Objectif : [UPLSAPO-40x2](https://www.olympus-lifescience.com/en/objectives/uplsapo/#!cms[tab]=%2Fobjectives%2Fuplsapo%2F40x2)

La roulette sur l'échantillon est le "cover slip compensation". J'imagine que ça éloigne la focale un peut pour avoir plus de jeu  à l'échantillon selon l'épaisseur du verre.

 

#### Manipulations

##### Trouver foyer

On met le gain du PMT a zéro. On place une feuille blanche sous l'échantillion et on peut voir le patern de la cible USAF environ au centre pour bien s'enligner. À l'aide de APT user sur l'ordinateur, on déplace la plaque qui a l'échantillon. La projection du patron de calibration sur la feuille de papier va zoomer jusqu'a temps que'on atteigne environ le focus, et l'image va dézoomer. Sachant la position approximative du focus, on augmente le gain jusqu'a ce quon voit le patron sur Scanimage. On peut ensuite descendre le step du moteur et ajuster la position de l'échantillon plus précisement en cherchant l'image avec les patrons les plus visible, en s'assurant de diminuer le gain pour ne pas saturer. Position sur APT user : -0.3922 , V range = 0.5

Oscilloscope : On voit un pic principal important a environ 10V et plusieurs petits pics qui suivent à environ 2V. L'intervalle en temps entre les pics est d'environ 60ns.

##### Résolution xy

Voici un tableau des images utilisée pour caractériser la résolution en x et en y pour différent zooms :

| Groupe et sous-groupe | Zoom | Moyenne | Nom fichier           | Résolution x (pixel, edge 90% a 10%) | Résolution y (pixel, edge 90% a 10%) | Pixel pour 1 ligne + un espace |
| --------------------- | ---- | ------- | --------------------- | ------------------------------------ | ------------------------------------ | ------------------------------ |
| 5-6 (17.54)           | x5   | 20      | edge_g5_l6_x5.tif     | 4.6                                  | 4.2                                  | 94±1                           |
| 7-6 (4.38)            | x8   | 20      | edge_g7_l1_x8.tif     | 6.0                                  | 5.8                                  | 34±1                           |
| 5-6                   | x2   | 20      | pixelres_g5_l6_x2.tif | 2.6                                  | 2.4                                  | 35±1                           |
| 5-6                   | x3   | 20      | edge_g5_l6_x3.tif     | 3.1                                  | 3.0                                  | 52±1                           |
| 5-6                   | x4   | 20      | edge_g5_l6_x4.tif     | 3.7                                  | 3.6                                  | 70±1                           |
| 7-1 (7.81)            | x6   | 20      | edge_g7_l1_x6.tif     | 4.7                                  | 4.5                                  | 47±1                           |
| 7-1                   | x7   | 20      | edge_g7_l1_x7.tif     | 5.3                                  | 5.1                                  | 53±1                           |

Avec ImageJ, on peut ensuite observer le profil des edges des lignes (edge transfer function). De plus, avec les memes images et les specs de la cible USAF, on peut déterminer un pixel en micron.  résolution : largeur de la edge transfer function (90% a 10%) en micron.

**Note : ne pas déplacer la plaque avec le "shift " sur ScanImage, cela désaligne les galvo.** Les galvo ont été désalignés et il a fallu les réalignés.



##### Mesure de la Edge Function

| Zoom | Champ de vue (um x um) | Résolution x (um) | Résolution y (um) |
| ---- | ---------------------- | ----------------- | ----------------- |
| x2   | 128.3 x 128.3          | 1.3               | 1.2               |
| x3   | 85.2 x 85.2            | 1.0               | 1.0               |
| x4   | 63.8 x 63.8            | 0.92              | 0.90              |
| x5   | 47.7 x 47.7            | 0.86              | 0.80              |
| x6   | 42.5 x 42.5            | 0.78              | 0.75              |
| x7   | 37.3 x 37.3            | 0.77              | 0.74              |
| x8   | 32.3 x 32.3            | 0.76              | 0.73              |

Graphique avec incertitudes

![resolutionxy](Confocal Microscopy/resolutionxy.PNG)

Plateau vers 6X. 

Cela pourrait avoir rapport avec la résolution numérique du système qui était limitante?

##### Résolution z

données : après avoir trouvé le focus, nous avons descendu de quelques microns et avont remonté par step de 500nm. Le noms des fichiers sont donc 00.tif, 05.tif, 10.tif, etc.

Les images initiales commencent très foncée est deviennent de plus en plus brillante plus on s'approche du focus. Toutefois, après avoir passé le focus, le images ne redeviennent pas tout a fait noire et on observe des "vagues de signal" sur la plaque. Ceci est probablement du a la plaque de resolution USAF qui n'est pas tout a fait droite et cela peut créer une perte de symétrie et de l'interférence. 

Champ de vue : 128x128 um, zoom = x2, vrange = 0.5

Graphique intensité en fonction déplacement en z, 0 = focus, positif = raproche de lobjectif

![unknown](Confocal Microscopy/unknown.png)

Les vagues sont probablement dûes à de l'interference entre deux réflections, cependant, l'étude poussée afin de s'assurer de cela dépasse le cadre de ce laboratoire. L'asymétrie de la distribution d'intensité est peut-être dûe à des aberrations qui dépacent les point focaux. Entre autre l'aberration sphérique qui est connue pour déplacer le centre du point focal devant ou derriere le point focal normal. Également l'astigmatisme éloigne le point focal sagital du point focal tangantiel, peut-être l'écartement de ces deux plan engenre un écartement de la distribution de la puissance sur l'axe???

##### Fluorescence

On remplace l'échantillon USAF par une feuille d'arbre. Étant donné qu'on est maintenant en fluorescence et que le signal de reflectance est plus important que le signal de fluorescence (malgré le miroir dichroique), il est important d'utiliser un filtre passe haut 650 nm pour couper le signal de réflectance.

Il est important d'ajuster la bague sur l'objectif qui prend compte du cover sur l'échantillon. La boite dit que ceux si sont entre 0.13 et 0.17mm d'épais, alors la bague est ajustée a 0.15 ce qui semble donner le meilleur résultat. Après avoir trouvé le focus, il faut mettre le gain et le laser au max pour voir quelques cellules.

ovocite : 0.4484 intervalle de 5 micron, zoom 1.5 pour voir la cellule au complet. On refait le focus et on prend des images a différentes hauteurs pour faire une reconstruction 3D de l'ovocite. 0.5 micron par pixel et on bouge de 5 micron = voxel depth de 10 

Les images d'ovocytes ne sont pas belles. La résolution du système n'est surement pas optimale, puisque d'autres images ont été prises avec un autre microscope et elles étaient beaucoup plus belles!



## Hi-Lo Microscopy

### Preparation

A review in detail of the phase contrast microscopy has been done. The anatomy of the microscope has also been made.

![microscope](HiLo Microscopy/microscope.PNG)

#### Hi-Lo

[Lien du résumé de la dernière équipe]()

##### fonctionnement de base de hilo :

permet de rejeter la lumière hors en combinant une image avec éclairage uniforme et une image a éclairage structuré (pattern, speckle)

**Ce qui a été fait :** principaux éléments du système d'illumination du microscope hilo ont été assemblé, mais certaines composantes doivent etre ajoutée/modifiée

Pièces importantes :

- camera DMK 21AF04

**Plan semaine 1 : **

- trouver un diffuseur qui fait des speckles de taille optimale (trouver cette taille) car plaque de verre et papier nettoyant ne sont pas ideals
- système d'éclairage uniforme (seulement léclairage structuré a été développé)
- relais 4f qui fait passer dia faisceau de 3cm a 6.35mm
- remplacer plaque de verre 4% reflexion par plaque ou cube 50%

#### Microscopie

##### Résumé et théorie :

##### Illumination de kholer:

- pas mettre miroir au plans conjugés, mettre au plan de fourier
- plan image de l'illumination doit avoir un condenseur pour brouiller l'image de la source lumineuse pour illumination uniforme
- vis du condenseur permet de positionner condenseur pour bien le mettre au plan image

##### Microscopie de phase:

- Permet de produire des images a haut constraste de spécimen transparents
- passage d'une onde dans un spécimen créé un déphasage et donc de l'interférence
- transforme décalage de phase causé par passage dans specimen par changement d'amplitude de la lumière a laide d'une plaque de phase. Interférence entre rayon principal et rayons difractés

**Questions de préparation : **

$$\Delta r \approx 1.22\frac{\lambda}{D}L\approx\frac{0.6\lambda}{\text{NA}}$$

pour lumière vert qui est environ 540nm et NA =1, on a 336nm.

### In Lab

#### Première séance

##### Ajustement du microscope 

1. la lumière qui sort du pied
2. on se place a x10
3. le diaphragme est ouvert et le microscope est mit en position O Le diphragme est situé DERRIERE la base.
4. Avec la grosse vis et puis la petite vis on atteint une image nette
5. Ensuite on ajuste le condenseur

##### Ajustement du condensateur :

Diaphragme de champ fermé au max, vis viagramme de champ = roulette veritcal noire derriere source lumineuse (dur a voir)

Vis pour déplacement vertical du condensateur : petite vis noire en dessous de la plaque. Vis xy, deux vis grise en doussous de celles du diaphragme

on centre polygone diaphragme de champ avec xy et on met au focus avec vis hauteur. on reouvre le diaphgramme a la grosseur du champ de vue, pas plus.

On ajuste le diaphgrame douverture pour avoir un équilibre entre résolution et contraste

##### Échantillons vivants :

Mettre 15 uL sur une lame puis deposser une lamelle de levure et de bactéries (2 lames dfférentes) Lame L =levures, lame B = bactéries

Levures : Amas de cellules

Levures x40:

![lev40](HiLo Microscopy/lev40.jpg)

Gros amas de cellule, noyau bien visible

Levures x100 avec huile:

![lev_100](HiLo Microscopy/lev_100.jpg)

Structure du noyau encore plus visible

On obseve des amas de cellules avec des cellules qui flottent autour, et quelques plus petites particules qui flottent. On observe un déplacment léger de ces cellules ainsi qu'une modification de la géométrie de leur cytoplasme (parfois)

##### Bactéries:

On met l'objectif 40x et lobjectif et ph4. avec la lentille de bertrand on alligne les aneaux du condensateur avec lanneau de phase de l'objectif. a x40 presque rien est visible, mais a x100 on voit des petits organismes qui grouille le long des bordures des bulles d'air. Objetif x100 nécessite de l'huile

Bactéries x40:

![bac40](HiLo Microscopy/bac40.jpg)

On remarque de petits points pâles, surtout près de la bordure noire. On pense que ceux-ci sont les bactéries puisque celles-ci sont très agités. Environ déplacement de 1/10 de l'image en 20 secondes

Bactéries x100 avec huile:

![bac100](HiLo Microscopy/bac100.jpg)

La lentille sur la caméra possède quelques saletés et poussières, qui sont visible au premier plan sur toutes les images. Nettoyage de la lentille serait necéssaire



#### Deuxième séance (HiLo)

##### Montage

Voici le montage ayant été conçu par les équipes avant nous:

![](HiLo Microscopy\montage_hilo_1.jpg)

Celui-ci apporte le laser jusqu'à l'objectif et grossit le faisceau 8x afin de remplir la BA de l'objectif.



##### Modifications

La première modification apportée au montage est l'ajout d'un beam splitter 50/50 afin de remplacer la lame de verre de 4/96 qui n'apportait qu'environ 3% de la puissance du laser à la caméra. Avec un 50/50, 25% de la lumière se rend jusqu'à la caméra.

![](C:\Users\marc-\Documents\GitHub\TPOB-GPH-4102\HiLo Microscopy\montage_split.jpg)

Ensuite, un échantillon très fluorescent devait être préparé, afin de savoir si vraiment il était possible de faire de la fluorescence avec ce microscope.  Des tests ont été faits en collaboration avec les gens du labo confocal sur des échantillons de marqueurs fluorescents. Puisque la source d'excitation est 633nm, on doit trouver un fluorophore qui est excité à cette longeur d'onde et qui émmet dans le vert environ. Après un essai avec 5 couleurs (orange, jaune, bleu, vert, violet) seul le violet s'est montré sensible. Voici l'image prise sous le microscope confocal:![](HiLo Microscopy\papel_confocal.jpg)

![](HiLo Microscopy\montage_papel.jpg)

Ainsi, un papier marqué au marqueur fluorescent violet a été placé sur une lamelle afin de pouvoir l'observer sous le microscope. 

Beaucoup de filtres ont été essayés; les mirroirs dichroiques du laboratoire, les filtres chromatiques, même le filtre du microscope confocal ne donnait rien.

***Le filtre utilisé dans le spectromètre a été emprunté par Daniel.*** 

Après fermeture des lumières et augmentation du temps d'exposition, une image de la fluorescence a pu être acquise:

![](HiLo Microscopy\papel.jpg)

Cela est faible, mais il s'agit bien de fibres du papier, car l'image ressemble beaucoup a celles prisent sur le microscope confocal. Excitation:633nm. Filtre: ???

##### à faire

Comme prochaine étape, il reste à

- Vérifier le filtre utilisé dans le spectromètre et vérifier qu'il est vraiment approprié pour le microscope
- Commander ce flitre et concevoir une monture appropriée, commander également les pièces.
- Ajuster l'alignement afin de ne pas avoir d'effet de vignetting
- Prendre une image avec et sans diffuseur pour esssayer l'algorithme du HiLo
- Trouver une monture mécanique pour le diffuseur



## Oximetry

### Preparation

fonctionnement du sphygmo-oxymètre:

- 2 diodes (red and IR) + photodiode

- Cardiac pulsation gorges veins with blood

- coefficient d'absorbtion change beaucoup en fonction du taux dHémoglobine/oxyhémoglobine et de la longeur d'onde

- Il s'agit de mesurer les ratios d'absobtion et de définir la concentration oxyhémoglobine

- Il y aura une composante stable (les tissus) et deux composantes changeantes avec le gonflement des veines.

  ![1542599699858](C:\Users\marc-\Documents\GitHub\TPOB-GPH-4102\HiLo Microscopy\hemo.PNG)



Loi de beer: décrit l'aténuation d'un signal tranversant un milieu homogène:

![](C:\Users\marc-\Documents\GitHub\TPOB-GPH-4102\HiLo Microscopy\beer.PNG)

à partir de cette loi, onretrouve la concentration en oxygène avec ces équations:

![](C:\Users\marc-\Documents\GitHub\TPOB-GPH-4102\HiLo Microscopy\calcul.PNG)

Circuit permettant la mesure oxymétrique proposé dans le protocol

![](HiLo Microscopy\montageschema.PNG)



Avant de monter le circuit, tester les différentes parties du circuit tel qu'indiqué dans le protocol de laboratoire

- Générateur de fonction
- Circuit de détection
- Filtre passe-bas du circuit
- Circuit et gain du transistor

### In Lab

#### Première Séance

Générateur de fonction : broche 4 et 2 branché a l'oscillo, 2.5V, 
​     temps UP = 11ms, temps DOWN = 19ms -> duty cycle = 11/30 = 36.7% _l¨l__l¨l
​     phase entre les 2 en degré = 168, devrait etre 120 pour cycle 33%

Broche 4 de la carte a broche 2 oxymètre, broche 2 carte a 3 oxymètre
​     On voit la DEL rouge qui clignote, mais on a pas assez de noirceur pour vérifier 
​     Ou est le ground?? : pas besoins, circuit flip et un devient ground de l'autre (insane)

**Discussion Dan :** 
transimpedance passe de source de courant (photodiode) à voltage
"facteur de gain" du transimpédance = resistance en haut = 1Mohm

haute fréquences (AC) ignore condensateur, le voit comme un fil
basse fréquences (DC) voit un circuit ouvert.
  -> filtre rc avec condensateur vers ground : passe bas, rc avec résistance vers ground = basse haut

condensateur vers ground = short le bruit haut fréquence : bypass condensator
Si fréquence plus petit que fréquence de coupure, on estime en DC

On essaye de faire ce circuit:

![](Oxymetry/400px-TIA_simple.png)



Le circuit de transimpédance est un circuit d'amplification qui permet de transformer un variation en courant en variation de tension. Son "gain" est mesuré en [V/A], ou encore en [Ohms]. Ce circuit possède une impédance d'entrée très faible et une impédance de sortie très élevée. Cela permet d'isoler la sortie du circuit d'amplification et d'utiliser la tension de sortie comme mesure ou comme signal de contrôle. L'amplificateur fonctionne de telle sorte qu'aucun courant n'entre dans les entrées + et -, mais la sortie de cet ampli essaie de ramener les deux entrée à la même tension. Ainsi, le courant qui passe dans la résistance $R_f$ est égale au courant $I_{in}$ et la tension de sortie est simplement $ V_{out} = I_r * R_f $. Ce type de circuit permet de réduire le bruit de mesure, est très stable et la mesure du "dark current" est nulle.

Ce circuit n'a pas marché, malgré plusieurs essaie. Peut-être un problème de ground. 

Ce circuit a été abandonné et une amplification simple a été

**Détection**
Fabrique le circuit de détection sans le filtre RC passe bas. On affiche le signal qu'on envoie a la DEL et le signal recu par la photodiode. 

```
- Signal DEL : carré expliqué dans générateur de fonction
- Signal recu : au départ, ligne horizontale et non ondes carré déphasé du signal DEL. On essaye de remplacer les                     pieces, mais en changenat le step vertical on voit des step mais qui ne sont pas tout à fait carré. 
- En ajoutant le cap-ranger, le signal est encore plus bruité initialement, et augmenter la capacitance transforme le signal carré l¨l_l¨l en vague /\/\/\. Ceci est lorsque l'op-amp est **fermé**.
- Lorsqu'on ouvre lalimentation du op-amp, le signal sature a environ 9V.
```

On remarque que pour que le courant DC continue, il faut un load au bout du courant avant l'oscilloscope, sinon le courant DC a nulpart ou aller. on ajoute 1kohm

De plus, On soupconne que le signal sature a cause que la résistance est trop grande. On la descend a 1Kohm
si on estime une puissance de 1mW de la Del, et photodiode génère environ 0.5A/W. on a donc 0.5mA ce qui devrait donner un voltage de V=RI = 0.5mA*1kOhm = 0.5V. On detecte toutefois 8.5V constant en dc, alors ou la DEL emet beaucoup plus ou il y a un probleme avec le circuit/l'ampliop. On descend la résistance a 100 Ohm, mais maintenant on a un courant DC qui est a 4.3V. Il semble donc que ce n'est pas un problème de saturation, surtout que l'expérience demande l'utilisation de 1MOhm au départ. On essaye a plusieurs reprises de changer des pièces, changer les ground, changer les résistances mais le signal a la sortie lorsque l'ampli-op est ouvert un toujours un signal DC. 
Le signal sans ampli-op semble suffisant? 

Si on met nottre doigt entre le load de 1kohm ajouté avant l'oscillscope et le résistance du trans impédance avec une certaine force, le signal devient carré et très stable. Si on pese plus fort le signal sature, si on pese moins fort le signal devient nul. Il faudrait donc augmenter la résistance?

#### Deuxième séance

On essaye une variation du circuit ou on remplace le transimpedance est enlevé et on utilise simplement une résistance.   Photo du circuit :



**Explication :** 
Reverse bias : 
Résistance choisie : 
Pas de condensateur : 

On est capable de voir des fonctions step a l'oscilloscope. Elles atteignent environ 500mV, on voit la variation du poul de quelques dizaines de mV et la différence entre le signal de rouge et ir capté de quelques dizaines de mV également. 



les battements du coeurs engendrent des variations de 20mV sur les 2 pulses (IR et RED) et on voit une différence entre l'intensité du signal en IR et en RED. La différence constante est de 20mV (plus haut pour les pulses IR). Voici une photo des oscilloscopes:

**PHOTO PERDUE**

Malheureusement, il n'a pas été possible de prendre des données significatives, trop de temps a été passé sur le debugage de l'électronique, on pense que peut-être les ampli sont brisés, à vérifier. Les données de l'oscilloscopes n'ont pas été enregistrées. L'expérience serait à recommencer avec des amplificateurs différents tel le OP-A380 ou le LM358 en utilisant une alimentation "rail to rail" et en lisant les datasheet en profondeur.





## Optical tweezers

### Preparation

Lecture du protocol en profondeur.

### In Lab

#### Première séance

#####  observation du montage

Le montage comporte 3 sous sytèmes; l'illumination, la détection de la position et la mesure de la force par rétroréflexion.

![](Pince Optique/Montage.PNG)

Le laser 5W infra-rouge permet de piéger la particule grace à une grande force de gradient qui dépasse la force de diffusion. (Déviation des photons et conservation de la quantité de mouvement) L'illumination rouge 633 (He-Ne) permet de mesurer la grandeur de la force et la position puisque l'intensité de la lumière diffusée celle-ci est proportionelle à la force et qui est relié à la position. Un photodiode à quadrant permet de trouver une équation qui permet de trouver la position de la bille.

l'illumination sur le dessus blanche permet d'avoir une image du système au plan focal capté par CCD.



**Discussion avec guillaume sur les plans conjugués et matrices**: Guillaume nous a explicité les termes ABCD du formalisme matriciel pour la propagation gaussienne avec l'approximation paraxiale. Entre autre, la condition d'imagerie a été discutée. Le terme B agit en fait comme condition sur le fait que le plan sera conjugué, parce que ce terme fera que les distances  des rayons par rapport à l'axe optique sera complètement indépendant des angles du système à ce plan. 

ON parle également de la correction des objectifs qui sont habituellement corrigés à l'infini.



##### Mesure des pentes de déplacement [V/mm]

Billes utilisées: polybeads polystyrene 5.9um



| Fichier  | Sens | Pente mesuré excel [V/pts] | Pente [V/mm] |
| -------- | ---- | -------------------------- | ------------ |
| Bille003 | y    | -2.87*10**-6               |              |
| Bille009 | x    | -8.64*10**-6               |              |



La vitesse du moteur en y : 0.003mm/s

La vitesse du moteur en x: 0.006mm/s

Vitesse d'acquisition 10kHz

Nombre d'acquisition 65000

Temps d'acquisition: 6.5s

distance parcourue y: 0.003*6.5 = 0.195mm

distance parcourue x: 0.006*6.5 = 0.39mm

Résolution Y: 65000/0.195= 333 333.3 points/mm

Résolution X: 65000/0.39 = 166 666.6 points/mm

Volts/mm en Y: $2.87\times10^{-6} \cdot 333 333.3 = -960V/m$

Volts/mm en Y: $8.64\times10^{-6} \cdot 166666.6 = 1440V/m$

 

Une première mesure de la constante de rappel a été faite. Le fichier donné est *rappel1.txt*.

#### Deuxième scéance

##### Mesure Constante de rappel

Maintenant, afin de s'assurer que cette constante de rapelle est connue, nous pourrions observer sa variation selon la puissance du laser infrarouge. De cette manière, pour de futures expériences, si la trappe optique est trop forte et que les déplacements ne peuvent être mesurés, la puissance du laser pourra être ajusté.

| **Puissance laser** [W] | fichier données | déplacement [m] | Constante k |
| ----------------------- | --------------- | --------------- | ----------- |
| 2.0W $\pm$              |                 | $\pm$           | $\pm$       |
| 2.5W $\pm$              |                 | $\pm$           | $\pm$       |
| 3.0W $\pm$              |                 | $\pm$           | $\pm$       |
| 3.5W $\pm$              |                 | $\pm$           | $\pm$       |
| 4.0W$\pm$               |                 | $\pm$           | $\pm$       |

*S'assurer d'écrire les incertitudes sur la puissance du laser et sur les déplacements en X pour pouvoir mettre une incertitude sur la force du moteur bactériel à la fin! Les incertitudes des éléments mesureés pourront être calculés par la suite, mais les incertitudes qu'on ne peut pas mesurer en dehors du lab doivent être prises en compte*

##### Mesures Sur la bactéries E.coli:

afin de déterminer la force du moteur bactériel de Ecoli, la même technique sera utilisée, la bactérie sera trapped, puis ses déplacement seront analysés. selon l'étalon mesuré avec la bille, on pourra déterminer la force qu'exerce la bactérie qui essaie de bouger.



##### Mesure de la vitesse de rotation de E.coli

.La plupart des bactéries seront immobiles, mais certaines tourneront sur
elles-même étant accrochées à la lamelle par leur filament (elles sont dites tethered). c'est avec celles-ci qu'on mesurera la vitesse de rotation.



##### Mesure du Couple du moteur flagellaire