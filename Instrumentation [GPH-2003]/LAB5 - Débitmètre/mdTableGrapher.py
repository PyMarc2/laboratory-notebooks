# code in collaboration with JLBegin

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)

zeroXFactor = 0

filename = "temps.txt"

with open(filename, "r") as file:
    lines = file.readlines()
    header = lines[0].split("|")[1:-1]
    numberOfCols = len(header)
    labels = [h.split("[")[0][1:-1] for h in header]
    info = [h.split("[")[1][:-2] for h in header]
    units = [i.split(" ")[0] for i in info]

    data = [[] for c in range(numberOfCols)]
    errors = [[] for c in range(numberOfCols)]
    defaultErrors = []

    for i in info:
        if len(i.split(" ")) > 1:
            defaultErrors.append(i.split(" ")[-1])
        else:
            defaultErrors.append(0)

    for line in lines[2:]:
        line = line.replace(" ", "").split("|")[1:-1]

        for i, cell in enumerate(line):
            cell = cell.split("$\\pm$")
            if len(cell) == 1:
                errors[i].append(float(defaultErrors[i]))
            else:
                errors[i].append(float(cell[1]))

            data[i].append(float(cell[0].replace("*", "")))

data[0] = [d - zeroXFactor for d in data[0]]
# bk = data[0][-1]
# data[0] = [np.arctan(d/48) for d in data[0]]
# factor = float(data[0][-1]/bk)
# errors[0] = [e*factor for e in errors[0]]

fig = plt.figure()
ax = fig.add_subplot(111)

# ========= TICKS SETTINGS ===========
majorLocator = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
xminorLocator = MultipleLocator(0.25)
yminorLocator = MultipleLocator(0.25)

#ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.set_xlim(-1, 11)
ax.tick_params()
# ====================================

for i, ylabel in enumerate(labels[1:]):
    slope, intercept, r_value, p_value, std_err = linregress(data[0], data[1+i])
    ylabel = "Fréquence de la sortie"
    ax.errorbar(data[0], data[1+i], xerr=errors[0], yerr=errors[1+i], marker=".", linestyle="", markersize=8, label="%s ($R^2=%.5f$)" % (ylabel, -1*round(r_value, 5)))
    #Linear regression
    ax.plot(data[0], np.multiply(slope, data[0])+intercept, label=("(%.1f $\pm$ %.1f)$\cdot$ $V_s$ + (%.1f $\pm$ %.1f)" % (round(slope, 1), 0.2, round(intercept, 1), 0.1)))

ax.set_xlabel("{} [{}]".format(labels[0], units[0]), fontsize=12)
ax.set_ylabel("{} [{}]".format(labels[1], units[1]), fontsize=12)

# ===== MANUAL SETTINGS =========
ax.set_ylabel("Temps de propagation [$\mu s$]")
ax.set_xlabel("Vitesse de l'air [$m/s$]")

ax.legend(loc='best', fontsize=11)
ax.grid(alpha=0.5, linestyle='--')
fig.set_size_inches(6, 6)
plt.show()
fig.savefig('temps.png', dpi=600)

