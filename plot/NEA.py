#!/usr/bin/env python
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import pandas as pd
import numpy as np
import os

# Number of outputs
Noutputs = 10000

# Initialize required arrays
diffa = np.ones((48, 9)) * np.nan
diffe = np.ones((48, 9)) * np.nan
aArr = np.ones((48, 9)) * np.nan
eArr = np.ones((48, 9)) * np.nan
ind1 = np.ones((48, 9)) * np.nan
ind2 = np.ones((48, 9)) * np.nan

# List of escaped particles
escBase = "../output/ordinary/output/escaped_"
paramBase = "../output/ordinary/output/parameters_"
escapes_19 = pd.read_csv(escBase + "19.csv")["particle"]
escapes_25 = pd.read_csv(escBase + "25.csv")["particle"]
# Loop over all asteroids
for i in range(1, 49):
    # Extract semi-major axis (a) and eccentricities (e)
    params = pd.read_csv(paramBase + str(i) + ".csv")
    a = params['a']
    e = params['e']

    # Exclude asteroid clones that escape the solar system
    if (i == 19):
        problemCloneNo = escapes_19 - 7
    elif (i == 25):
        problemCloneNo = escapes_25 - 7
    else:
        problemCloneNo = np.ones((3,1))*-1
    for j in range(0, 9):
        if (problemCloneNo[0] == -1 or np.sum(j == problemCloneNo) == 0):
            diffa[i-1, j] = a[79999 + Noutputs*j]-a[70000 + Noutputs*j]
            diffe[i-1, j] = e[79999 + Noutputs*j]-e[70000 + Noutputs*j]
            aArr[i-1, j] = a[79999 + Noutputs*j]
            eArr[i-1, j] = e[79999 + Noutputs*j]
            ind1[i-1, j] = i
            ind2[i-1, j] = j

# Remove NaN entries and flatten 2d array into 1d so we can plot them
diffa = diffa[np.logical_not(np.isnan(diffa))]
diffa = diffa.flatten()
diffe = diffe[np.logical_not(np.isnan(diffe))]
diffe = diffe.flatten()
aArr = aArr[np.logical_not(np.isnan(aArr))]
aArr = aArr.flatten()
eArr = eArr[np.logical_not(np.isnan(eArr))]
eArr = eArr.flatten()
ind1 = ind1[np.logical_not(np.isnan(ind1))]
ind1 = ind1.flatten()
ind2 = ind2[np.logical_not(np.isnan(ind2))]
ind2 = ind2.flatten()

# First figure with semi-major axis difference used for colour gradient
fig1 = plt.figure(1, figsize=(8, 6))
ax1 = fig1.add_subplot(111)
p1 = ax1.scatter(aArr, eArr, c=diffa, label="Final value")
cbar1 = fig1.colorbar(p1)
cbar1.set_label('Semi-major axis difference', size=24)
cbar1.ax.tick_params(labelsize=14)
N=20
x1 = 2.502*np.ones((N, 1))
x2 = np.linspace(0.01, 0.28, N)
y1 = x2
ax1.scatter(x1, y1, marker='*', label="Kirkwood gap")
plt.xlim([2.36, 2.51])
plt.ylim([0, 0.29])
plt.xlabel("Semi-major axis (au)", fontsize=24)
plt.xticks(fontsize=16)
plt.ylabel("Eccentricity", fontsize=24)
plt.yticks(fontsize=16)
plt.title("Eccentricity vs semi-major axis plot", fontsize=26)
plt.legend(loc="best", fontsize=16)
ESMABase = "../plots/Eccentricity_vs_semimajor_axis/"
svgtitle1 = ESMABase + "SMA_colour_grade_all_clones.svg"
pngtitle1 = ESMABase + "SMA_colour_grade_all_clones.png"
plt.savefig(svgtitle1)
os.system("convert {} {}".format(svgtitle1, pngtitle1))
plt.close()

# Second figure with eccentricity difference used for colour gradient
fig2 = plt.figure(2, figsize=(8, 6))
ax2 = fig2.add_subplot(111)
p2 = ax2.scatter(aArr, eArr, c=diffe, label="Final value")
cbar2 = fig2.colorbar(p2)
cbar2.set_label("Eccentricity difference", size=24)
cbar2.ax.tick_params(labelsize=14)
ax2.scatter(x1, y1, marker='*', label="Kirkwood gap")
plt.xlim([2.36, 2.51])
plt.ylim([0, 0.29])
plt.xlabel("Semi-major axis (au)", fontsize=24)
plt.xticks(fontsize=16)
plt.ylabel("Eccentricity", fontsize=24)
plt.yticks(fontsize=16)
plt.title("Eccentricity vs semi-major axis plot", fontsize=26)
plt.legend(loc="best", fontsize=16)
svgtitle2 = ESMABase + "E_colour_grade_all_clones.svg"
pngtitle2 = ESMABase + "E_colour_grade_all_clones.png"
plt.savefig(svgtitle2)
os.system("convert {} {}".format(svgtitle2, pngtitle2))
plt.close()
