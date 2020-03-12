import matplotlib.pyplot as plt
import glob
from ERF import analyze_edge
from scipy.interpolate import UnivariateSpline

files = glob.glob("data/ERF*.csv")

# fixme: weird result from 40 projs centered giving better MTF (40 > 320 > 160)

origs = []
erffits = []
psfs = []
mtfs = []
mtfs_01 = []
mtfs_us = []

for file in files:
    print(file)
    voxelsize = float(file.split("_")[4])

    orig, erffit, psf, mtf = analyze_edge(file, voxelsize, skipPlots=False)
    mtf_us = UnivariateSpline(mtf[0], mtf[1] - 0.1, k=3, s=0)
    mtf_01 = mtf_us.roots()[-1]

    mtfs_01.append((file, mtf_01))
    mtfs_us.append(mtf_us)
    origs.append(orig)
    erffits.append(erffit)
    psfs.append(psf)
    mtfs.append(mtf)

plt.figure("mtf haut bas 2d")
plt.plot(mtfs[17][0], mtfs[17][1], label="bas", ls="-", lw=2, color="tab:orange")
plt.plot(mtfs[18][0], mtfs[18][1], label="haut", ls="-.", lw=2, color="tab:blue")
plt.plot(mtfs[19][0], mtfs[19][1], label="centre", ls="--", lw=2, color="tab:green")
plt.legend(loc="best", fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
plt.ylabel("MTF($f$)", fontsize=24)
plt.xlim(0, 2.5)
plt.tight_layout()
plt.savefig("figures/mtf_haut_bas_2d.png", dpi=400)

plt.figure("mtf eventail")
plt.plot(mtfs[5][0], mtfs[5][1], label="Conique", ls="-", lw=2, color="tab:orange")
plt.plot(mtfs[16][0], mtfs[16][1], label="Éventail 1.5 cm", ls="-.", lw=2, color="tab:blue")
plt.plot(mtfs[15][0], mtfs[15][1], label="Éventail 0.5 cm", ls="--", lw=2, color="tab:green")
plt.legend(loc="best", fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
plt.ylabel("MTF($f$)", fontsize=24)
plt.xlim(0, 0.5)
plt.tight_layout()
plt.savefig("figures/mtf_eventail.png", dpi=400)

plt.figure("erf haut bas 2d")
plt.plot(erffits[17][0], erffits[17][1], label="bas", ls="-", lw=2, color="blue")
plt.plot(erffits[18][0], erffits[18][1], label="haut", ls="-.", lw=2, color="red")
plt.plot(erffits[19][0], erffits[19][1], label="centre", ls="--", lw=2, color="g")
plt.legend(loc="best", fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel("Position [mm]", fontsize=24)
plt.ylabel("ERF($x$)", fontsize=24)
plt.margins(0.05)
plt.tight_layout()
plt.savefig("figures/erf_haut_bas_2d.png", dpi=200)

plt.figure("erf haut bas 3d")
plt.plot(erffits[3][0], erffits[3][1], label="bas", ls="-", lw=2, color="blue")
plt.plot(erffits[4][0], erffits[4][1], label="haut", ls="-.", lw=2, color="red")
plt.plot(erffits[5][0], erffits[5][1], label="centre", ls="--", lw=2, color="g")
plt.legend(loc="best", fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel("Position [mm]", fontsize=24)
plt.ylabel("ERF($x$)", fontsize=24)
plt.margins(0.05)
plt.tight_layout()
plt.savefig("figures/erf_haut_bas_3d.png", dpi=200)


fig, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(12, 4))

# plt.figure("mtf haut bas 3d")
ax1.plot(mtfs[3][0], mtfs[3][1], label="bas", ls="-", color="tab:orange")
ax1.plot(mtfs[4][0], mtfs[4][1], label="haut", ls="-.", color="tab:blue")
ax1.plot(mtfs[5][0], mtfs[5][1], label="centre", ls="--", color="tab:green")
ax1.legend(loc="best", fontsize=12)
ax1.tick_params(labelsize=12)
ax1.set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
ax1.set_ylabel("MTF($f$)", fontsize=12)
ax1.set_xlim(0, 0.5)
# ax1.tight_layout()
# ax1.savefig("figures/mtf_haut_bas_3d.png", dpi=200)
ax1.text(-0.09, 1.02, "C", transform=ax1.transAxes, size=16, weight='bold')

# plt.figure("mtf 0.25 vs 0.5 vs 2")
ax2.plot(mtfs[11][0], mtfs[11][1], label="voxels de 2mm", ls="-", color="tab:orange")
ax2.plot(mtfs[8][0], mtfs[8][1], label="voxels de 0.5mm", ls="-.", color="tab:blue")
ax2.plot(mtfs[5][0], mtfs[5][1], label="voxels de 0.25mm", ls="--", color="tab:green")
ax2.legend(loc="best", fontsize=12)
ax2.tick_params(labelsize=12)
ax2.set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
ax2.set_ylabel("MTF($f$)", fontsize=12)
ax2.set_xlim(0, 0.5)
# ax1.tight_layout()
# ax1.savefig("figures/mtf_taille_voxels_3d_edge", dpi=200)
# ax2.text(-0.09, 1.02, "B", transform=ax2.transAxes, size=16, weight='bold')

# plt.figure("mtf num proj edge")
ax3.plot(mtfs[13][0], mtfs[13][1], label="40 proj.", ls="-", color="tab:orange")
ax3.plot(mtfs[2][0], mtfs[2][1], label="160 proj.", ls="-.", color="tab:blue")
ax3.plot(mtfs[5][0], mtfs[5][1], label="320 proj.", ls="--", color="tab:green")
ax3.legend(loc="best", fontsize=12)
ax3.tick_params(labelsize=12)
ax3.set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
ax3.set_ylabel("MTF($f$)", fontsize=12)
ax3.set_xlim(0, 0.5)
# ax2.tight_layout()
# ax2.savefig("figures/mtf_num_proj_edge", dpi=200)
# ax3.text(-0.09, 1.02, "C", transform=ax3.transAxes, size=16, weight='bold')

plt.tight_layout()
plt.savefig("figures/mtf_combo_pos_taille_proj", dpi=600)

plt.figure("erf num proj edge")
plt.plot(erffits[13][0], erffits[13][1], label="40 proj.", ls="-", lw=2, color="blue")
plt.plot(erffits[2][0], erffits[2][1], label="160 proj.", ls="-.", lw=2, color="red")
plt.plot(erffits[5][0], erffits[5][1], label="320 proj.", ls="--", lw=2, color="g")
plt.legend(loc="best", fontsize=20)
plt.tick_params(labelsize=20)
plt.xlabel("Position [mm]", fontsize=24)
plt.ylabel("ERF($x$)", fontsize=24)
plt.margins(0.05)
plt.tight_layout()
plt.savefig("figures/erf_num_proj_edge", dpi=200)

"""
res = 
0 data\ERF_CT_conique_160_0.25_bas.csv
1 data\ERF_CT_conique_160_0.25_haut.csv
2 data\ERF_CT_conique_160_0.25_milieu.csv   (proj)
3 data\ERF_CT_conique_320_0.25_bas.csv      (pos)
4 data\ERF_CT_conique_320_0.25_haut.csv     (pos)
5 data\ERF_CT_conique_320_0.25_milieu.csv   (res, proj, pos)
6 data\ERF_CT_conique_320_0.5_bas.csv
7 data\ERF_CT_conique_320_0.5_haut.csv
8 data\ERF_CT_conique_320_0.5_milieu.csv    (res)
9 data\ERF_CT_conique_320_2_bas.csv
10 data\ERF_CT_conique_320_2_haut.csv
11 data\ERF_CT_conique_320_2_milieu.csv     (res)
12 data\ERF_CT_conique_40_0.25_bas.csv
13 data\ERF_CT_conique_40_0.25_haut.csv
14 data\ERF_CT_conique_40_0.25_milieu.csv   (proj) * switch to 13
15 data\ERF_CT_eventail0.5_320_0.25_milieu.csv
16 data\ERF_CT_eventail1.5_320_0.25_milieu.csv
17 data\ERF_Radio_bas.csv
18 data\ERF_Radio_haut.csv
19 data\ERF_Radio_milieu.csv
"""


""" PSF (X) et MTF (F) """

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0][0].plot(psfs[3][0], psfs[3][1], label="bas", ls="-", color="tab:orange")
axes[0][0].plot(psfs[4][0], psfs[4][1], label="haut", ls="-.", color="tab:blue")
axes[0][0].plot(psfs[5][0], psfs[5][1], label="centre", ls="--", color="tab:green")
axes[0][0].legend(loc="best", fontsize=12)
axes[0][0].tick_params(labelsize=12)
axes[0][0].set_xlabel("Position $x$ [mm]", fontsize=12)
axes[0][0].set_ylabel("PSF(x)", fontsize=12)
axes[0][0].set_xlim(-10, 10)

axes[0][0].text(-0.09, 1.02, "A", transform=axes[0][0].transAxes, size=16, weight='bold')

axes[0][1].plot(psfs[11][0], psfs[11][1], label="2.0mm", ls="-", color="tab:orange")
axes[0][1].plot(psfs[8][0], psfs[8][1], label="0.5mm", ls="-.", color="tab:blue")
axes[0][1].plot(psfs[5][0], psfs[5][1], label="0.25mm", ls="--", color="tab:green")
axes[0][1].legend(loc="best", fontsize=12)
axes[0][1].tick_params(labelsize=12)
axes[0][1].set_xlabel("Position $x$ [mm]", fontsize=12)
axes[0][1].set_ylabel("PSF(x)", fontsize=12)
axes[0][1].set_xlim(-10, 10)

axes[0][2].plot(psfs[13][0]+2.9, psfs[13][1], label="40 proj.", ls="-", color="tab:orange")
axes[0][2].plot(psfs[2][0]+0.2, psfs[2][1], label="160 proj.", ls="-.", color="tab:blue")
axes[0][2].plot(psfs[5][0], psfs[5][1], label="320 proj.", ls="--", color="tab:green")
axes[0][2].legend(loc="best", fontsize=12)
axes[0][2].tick_params(labelsize=12)
axes[0][2].set_xlabel("Position $x$ [mm]", fontsize=12)
axes[0][2].set_ylabel("PSF(x)", fontsize=12)
axes[0][2].set_xlim(-10, 10)


axes[1][0].plot(mtfs[3][0], mtfs[3][1], label="bas", ls="-", color="tab:orange")
axes[1][0].plot(mtfs[4][0], mtfs[4][1], label="haut", ls="-.", color="tab:blue")
axes[1][0].plot(mtfs[5][0], mtfs[5][1], label="centre", ls="--", color="tab:green")
axes[1][0].legend(loc="best", fontsize=12)
axes[1][0].tick_params(labelsize=12)
axes[1][0].set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
axes[1][0].set_ylabel("MTF($f$)", fontsize=12)
axes[1][0].set_xlim(0, 0.5)

axes[1][0].text(-0.09, 1.02, "B", transform=axes[1][0].transAxes, size=16, weight='bold')

axes[1][1].plot(mtfs[11][0], mtfs[11][1], label="voxels de 2mm", ls="-", color="tab:orange")
axes[1][1].plot(mtfs[8][0], mtfs[8][1], label="voxels de 0.5mm", ls="-.", color="tab:blue")
axes[1][1].plot(mtfs[5][0], mtfs[5][1], label="voxels de 0.25mm", ls="--", color="tab:green")
axes[1][1].legend(loc="best", fontsize=12)
axes[1][1].tick_params(labelsize=12)
axes[1][1].set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
axes[1][1].set_ylabel("MTF($f$)", fontsize=12)
axes[1][1].set_xlim(0, 0.5)

axes[1][2].plot(mtfs[13][0], mtfs[13][1], label="40 proj.", ls="-", color="tab:orange")
axes[1][2].plot(mtfs[2][0], mtfs[2][1], label="160 proj.", ls="-.", color="tab:blue")
axes[1][2].plot(mtfs[5][0], mtfs[5][1], label="320 proj.", ls="--", color="tab:green")
axes[1][2].legend(loc="best", fontsize=12)
axes[1][2].tick_params(labelsize=12)
axes[1][2].set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=12)
axes[1][2].set_ylabel("MTF($f$)", fontsize=12)
axes[1][2].set_xlim(0, 0.5)

plt.tight_layout()
plt.savefig("figures/psf-mtf_combo_pos_taille_proj", dpi=600)


""" ERF Annexe """
# fig, axes = plt.subplots(3, 3, figsize=(8, 8))
#
# # data\ERF_CT_conique_320_0.5_milieu.csv    (res)
# j = 0
# for i, file in enumerate(files):
#     if "milieu" in file:
#         axes[j//3, j%3].plot(origs[i][0], origs[i][1], label="mesurée", lw=1, color="blue")
#         axes[j//3, j%3].plot(erffits[i][0], erffits[i][1], label="ajustée", lw=1, color="red", ls="--")
#         # axes[j//3, j%3].legend(loc="best")
#         if "conique" in file:
#             title = "F.C. {} p. {}mm".format(*file.split("_")[3:-1])
#         elif "Radio" in file:
#             title = "Projection 2D"
#         else:
#             title = "F.E. {} p. {}mm".format(*file.split("_")[3:-1])
#         axes[j//3, j%3].set_title(title, fontsize=10)
#         axes[j//3, j%3].set_xlabel("Position $x$ [mm]", fontsize=10)
#         axes[j//3, j%3].set_ylabel("ERF", fontsize=10)
#         axes[j // 3, j % 3].tick_params(labelsize=9)
#         axes[j//3, j%3].set_ylim(0, 1)
#         axes[j // 3, j % 3].set_xlim(10, 50)
#         j += 1
#         # axes[j//3, j%3].tick_params(labelsize=20)
# plt.margins(0.05)
# plt.tight_layout()
# plt.savefig("figures/erf_annexe", dpi=600)
