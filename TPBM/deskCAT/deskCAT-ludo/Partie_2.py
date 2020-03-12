import matplotlib.pyplot as plt
import numpy as np
from matplotlib.transforms import ScaledTranslation

LargeurDiaphragme = [0.5, 1, 1.5, 5.2]
ErrDiaphragme = [0.1, 0.1, 0.1, 0.1]

#Les doigts sont numérotés de 1 à 4 et en ordre croissant de taille
Doigt1 = np.array([1.2256, 1.1430, 1.0487, 0.9927])
Doigt2 = np.array([1.3275, 1.1300, 1.1529, 0.9898])
Doigt3 = np.array([1.3292, 1.2086, 1.1583, 1.0545])
Doigt4 = np.array([1.3577, 1.2544, 1.1941, 1.0978])

SigmaDoigt1 = np.array([0.1333, 0.0932, 0.1171, 0.0939])
SigmaDoigt2 = np.array([0.0836, 0.1522, 0.0274, 0.1478])
SigmaDoigt3 = np.array([0.059, 0.0669, 0.048, 0.0911])
SigmaDoigt4 = np.array([0.0506, 0.0136, 0.0097, 0.0597])

fig, ax = plt.subplots()
trans1 = ax.transData + ScaledTranslation(-8/72, 0, fig.dpi_scale_trans)
trans2 = ax.transData + ScaledTranslation(-3/72, 0, fig.dpi_scale_trans)
trans3 = ax.transData + ScaledTranslation(+3/72, 0, fig.dpi_scale_trans)
trans4 = ax.transData + ScaledTranslation(+8/72, 0, fig.dpi_scale_trans)

er1 = ax.errorbar(LargeurDiaphragme, Doigt1, transform=trans1, fmt='.', xerr=ErrDiaphragme, yerr=SigmaDoigt1, label='Doigt 1')
er2 = ax.errorbar(LargeurDiaphragme, Doigt2, transform=trans2, fmt='^', xerr=ErrDiaphragme, yerr=SigmaDoigt2, label='Doigt 2')
er3 = ax.errorbar(LargeurDiaphragme, Doigt3, transform=trans3, fmt='s', xerr=ErrDiaphragme, yerr=SigmaDoigt3, label='Doigt 3')
er4 = ax.errorbar(LargeurDiaphragme, Doigt4, transform=trans4, fmt='v', xerr=ErrDiaphragme, yerr=SigmaDoigt4, label='Doigt 4')

plt.xlabel('Largeur du diaphragme $[cm]$', fontsize=15)
plt.ylabel("Coefficient d'atténuation $\mu$ $[cm^{-1}]$", fontsize=16)
plt.tick_params(labelsize=12)
plt.legend()
plt.savefig("figures/Mu_vs_diaphragme", dpi=200)