import matplotlib.pyplot as plt
import numpy as np

table = np.loadtxt("data/p4.txt", dtype=str, delimiter=";")
table = np.delete(table, [5, 6], axis=1)

head = table[0, 1:]
data = table[1:, 1:]
f = np.asarray(table[1:, 0], dtype=float)


def getMTF(lineData):
    res = []
    for r in lineData:
        if r != "-":
            high, low = map(float, r.split("/"))
            res.append((high-low) / (high + low))
    return res


fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(8, 4.2))

for i, label in enumerate(head):
    mtf = getMTF(data[:, i])
    errors = np.full(len(mtf), mtf[0]*0.08)  # decent arbitrary error of 8 % (no variance noted for these data series)

    ax = ax1 if i < 4 else ax2
    j = i % 4
    spacing = j/150

    ax.errorbar(f[:len(mtf)]+spacing, mtf, yerr=errors, label=label, linestyle="",
                marker=["v", "x", "o", "D"][j], color=["tab:orange", "tab:blue", "tab:green", "tab:red"][j],
                markersize=[6, 6, 5, 5][j], capsize=2, elinewidth=1)

    ax.set_xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=15)  # , fontsize=24)
    ax.set_ylabel("MTF($f$)", fontsize=15)  # , fontsize=24)
    ax.tick_params(labelsize=15)
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=12)

ax1.text(-0.09, 1.02, "A", transform=ax1.transAxes, size=16, weight='bold')
ax2.text(-0.09, 1.02, "B", transform=ax2.transAxes, size=16, weight='bold')
plt.tight_layout()
plt.savefig("figures/fig_partie_4.png", dpi=600)
