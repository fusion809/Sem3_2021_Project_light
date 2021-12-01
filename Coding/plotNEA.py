#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Number of outputs
Noutputs = 10000

# Initialize required arrays
diffa = np.ones((48, 9)) * np.nan
diffe = np.ones((48, 9)) * np.nan
a_arr = np.ones((48, 9)) * np.nan
e_arr = np.ones((48, 9)) * np.nan

# List of escaped particles
escapes_19 = pd.read_csv("output/ordinary/output/escaped_19.csv")["particle"]
escapes_25 = pd.read_csv("output/ordinary/output/escaped_25.csv")["particle"]
# Loop over all asteroids
for i in range(1, 49):
    # Extract semi-major axis (a) and eccentricities (e)
    params = pd.read_csv("output/ordinary/output/parameters_" + str(i) + ".csv")
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
            a_arr[i-1, j] = a[79999 + Noutputs*j]
            e_arr[i-1, j] = e[79999 + Noutputs*j]

# Remove NaN entries and flatten 2d array into 1d so we can plot them
diffa = diffa[np.logical_not(np.isnan(diffa))]
diffa = diffa.flatten()
diffe = diffe[np.logical_not(np.isnan(diffe))]
diffe = diffe.flatten()
a_arr = a_arr[np.logical_not(np.isnan(a_arr))]
a_arr = a_arr.flatten()
e_arr = e_arr[np.logical_not(np.isnan(e_arr))]
e_arr = e_arr.flatten()

# First figure with semi-major axis difference used for colour gradient
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
p1 = ax1.scatter(a_arr, e_arr, c=diffa)
fig1.colorbar(p1, label="Semi-major axis difference")
plt.xlabel("Semi-major axis (AU)")
plt.ylabel("Eccentricity")
plt.title("Eccentricity vs semi-major axis plot")
plt.savefig("plots/Eccentricity_vs_semimajor_axis_SMA_colour_grade_all_clones.svg")
plt.close()

# Second figure with eccentricity difference used for colour gradient
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
p2 = ax2.scatter(a_arr, e_arr, c=diffe)
fig2.colorbar(p2, label="Eccentricity difference")
plt.xlabel("Semi-major axis (AU)")
plt.ylabel("Eccentricity")
plt.title("Eccentricity vs semi-major axis plot")
plt.savefig("plots/Eccentricity_vs_semimajor_axis_E_colour_grade_all_clones.svg")
plt.close()
