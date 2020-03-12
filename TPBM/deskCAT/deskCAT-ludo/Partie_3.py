import numpy as np
import matplotlib.pyplot as plt

Mu0visible = np.array([1.0244, 1.1315, 1.3725, 1.9727, 2.1643, 2.0197])
ErrMu0visible = np.array([0.1594, 0.2268, 0.3752, 0.6856, 0.8003, 0.9259])
Mu0invisible = np.array([0.2784, 0.2755, 0.2871, 0.3739, 0.5072, 0.7332])
ErrMu0invisible = np.array([0.039, 0.0780, 0.1444, 0.3211, 0.4473, 0.6128])

MuB = np.array([0.0603, 0.0513, 0.1225, 0.1888, 0.2673, 0.3434])
SigmaB = np.array([0.0864, 0.0864, 0.1537, 0.2583, 0.3699, 0.4890])

CNRvisible = (Mu0visible - MuB)/SigmaB
ErrCNRvisible = ErrMu0visible/SigmaB + 1

CNRinvisible = (Mu0invisible - MuB)/SigmaB
ErrCNRinvisible = ErrMu0invisible/SigmaB + 1

print(CNRinvisible, CNRvisible)

BruitGaussien = np.array([1, 2, 3, 6, 10, 20])

plt.errorbar(BruitGaussien, CNRvisible, fmt='^',  yerr=ErrCNRvisible, label='Cône le plus contrasté')
plt.errorbar(BruitGaussien, CNRinvisible, fmt='v', yerr=ErrCNRinvisible, label='Cône le moins contrasté')
plt.xlabel('Bruit gaussien ajouté au données [%]', fontsize=15)
plt.ylabel('Rapport contraste sur bruit CNR [-]', fontsize=15)
plt.legend()
plt.tick_params(labelsize=12)
plt.savefig("figures/CNR_vs_Bruit", dpi=200)
