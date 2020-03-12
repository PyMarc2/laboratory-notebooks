import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

MuMoy3DRouge = np.array([0.0005, 0.1299, 0.2285, 0.2873, 0.3184, 0.3110, 0.3041, 0.2993])
DevStandMu3DRouge = np.array([0.0006, 0.0028, 0.0043, 0.0073, 0.0123, 0.016, 0.0176, 0.015])
Mu2DRouge = [0.000257, 0.1555, 0.274, 0.354, 0.435, 0.468, 0.481, 0.487]
VolSolutionOpaqueRouge = np.array([0, 1, 2, 3, 5, 7.5, 10, 15])
ErrVolRouge = [0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

MuMoy3DVert = [0.0004, 0.0486, 0.0994, 0.1439, 0.2335, 0.2881, 0.3217, 0.3432]
DevStandMu3DVert = [0.0006, 0.0028, 0.0023, 0.0022, 0.0046, 0.0062, 0.008, 0.0129]
Mu2DVert = [0.008, 0.0613, 0.1151, 0.1634, 0.252, 0.3319, 0.3939, 0.4604]
VolSolutionOpaqueVert = [0, 1, 2, 3, 5, 7.5, 10, 15]
ErrVolVert = [0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

VolNew = np.linspace(0, 15, 100)
MuNew = np.linspace(0, 0.4, 100)

# def polynôme(x, a, b, c, d, e, f, g, h):
#     return h*x**7 + g*x**6 + f*x**5 + e*x**4 + a*x**3 + b*x**2 + c*x + d

def polynôme(x, a, b):
    return np.multiply(a,x) + b

popt3DRouge, pcov3DRouge = curve_fit(polynôme, VolSolutionOpaqueRouge[0:3], MuMoy3DRouge[0:3], sigma=[i*2 for i in DevStandMu3DRouge[0:3]])
popt2DRouge, pcov2DRouge = curve_fit(polynôme, VolSolutionOpaqueRouge[0:3], Mu2DRouge[0:3])
popt3DVert, pcov3DVert = curve_fit(polynôme, VolSolutionOpaqueVert[0:5], MuMoy3DVert[0:5], sigma=[i*2 for i in DevStandMu3DVert[0:5]])
popt2DVert, pcov2DVert = curve_fit(polynôme, VolSolutionOpaqueVert[0:5], Mu2DVert[0:5])

splRed3D = make_interp_spline(VolSolutionOpaqueRouge, MuMoy3DRouge, k=3)
Red3D_smooth = splRed3D(VolNew)
splRed2D = make_interp_spline(VolSolutionOpaqueRouge, Mu2DRouge, k=3)
Red2D_smooth = splRed2D(VolNew)

splVert3D = make_interp_spline(VolSolutionOpaqueVert, MuMoy3DVert, k=3)
Vert3D_smooth = splVert3D(VolNew)
splVert2D = make_interp_spline(VolSolutionOpaqueVert, Mu2DVert, k=3)
Vert2D_smooth = splVert2D(VolNew)

plt.errorbar(VolSolutionOpaqueRouge, MuMoy3DRouge, fmt='.', color='firebrick', xerr=ErrVolRouge, yerr=np.array([i*2 for i in DevStandMu3DRouge]))
plt.errorbar(VolSolutionOpaqueRouge, Mu2DRouge, fmt='.', color='red', xerr=ErrVolRouge)
plt.plot(VolSolutionOpaqueRouge[0:3], polynôme(VolSolutionOpaqueRouge[0:3], *popt3DRouge), label='$\mu_{{3DRouge}} = ax +b$'.format(*popt3DRouge), color='firebrick')
plt.plot(VolSolutionOpaqueRouge[0:3], polynôme(VolSolutionOpaqueRouge[0:3], *popt2DRouge), label='$\mu_{{2DRouge}} = ax +b$'.format(*popt2DRouge), color='lightcoral')
plt.plot(VolNew, Red3D_smooth, color='firebrick', linestyle='--', alpha=0.7)
plt.plot(VolNew, Red2D_smooth, color='lightcoral', linestyle='--', alpha=0.7)

plt.errorbar(VolSolutionOpaqueVert, MuMoy3DVert, fmt='.', color='darkgreen', xerr=ErrVolVert, yerr=np.array([i*2 for i in DevStandMu3DVert]))
plt.errorbar(VolSolutionOpaqueVert, Mu2DVert, fmt='.', color='lime', alpha=0.7, xerr=ErrVolVert)
plt.plot(VolSolutionOpaqueVert[0:5], polynôme(VolSolutionOpaqueVert[0:5], *popt3DVert), label='$\mu_{{3DVert}} = ax +b$'.format(*popt3DVert), color='darkgreen')
plt.plot(VolSolutionOpaqueVert[0:5], polynôme(VolSolutionOpaqueVert[0:5], *popt2DVert), label='$\mu_{{2DVert}} = ax +b$'.format(*popt2DVert), color='lime')
plt.plot(VolNew, Vert3D_smooth, color='darkgreen', linestyle='--', alpha=0.7)
plt.plot(VolNew, Vert2D_smooth, color='lime', linestyle='--', alpha=0.7)

plt.xlabel('Volume de solution opaque [mL]', fontsize=20)
plt.ylabel("Coefficient d'atténuation $\mu$ $[cm^{-1}]$", fontsize=20)
# plt.legend(loc='best', fontsize=13)
plt.tick_params(labelsize=18)
plt.gcf().set_size_inches(10, 6)
plt.savefig('figures/Mu_vs_Volume', dpi=200)