#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Noutputs = 10000

diffa = np.zeros((48, 9))
diffe = np.zeros((48, 9))
a_arr = np.zeros((48, 9))
e_arr = np.zeros((48, 9))
for i in range(1, 49):
    params = pd.read_csv("output/ordinary/output/parameters_" + str(i) + ".csv")
    a = params['a']
    e = params['e']
    for j in range(0, 9):
        diffa[i-1, j] = a[79999 + Noutputs*j]-a[70000 + Noutputs*j]
        diffe[i-1, j] = e[79999 + Noutputs*j]-e[70000 + Noutputs*j]
        a_arr[i-1, j] = a[79999 + Noutputs*j]
        e_arr[i-1, j] = e[79999 + Noutputs*j]

# First figure
plt.figure(1)
plt.scatter(a_arr[:,1], e_arr[:,1], c=diffa[:,1])
plt.xlabel("Semi-major axis (AU)")
plt.ylabel("Eccentricity")
plt.title("Eccentricity vs semi-major axis (colour graded according to SMA difference) clone 1")
plt.savefig("plots/Eccentricity_vs_semimajor_axis_SMA_colour_grade_clone1.svg")
plt.close()

plt.figure(2)
plt.scatter(a_arr[:,1], e_arr[:,1], c=diffe[:,1])
plt.xlabel("Semi-major axis (AU)")
plt.ylabel("Eccentricity")
plt.title("Eccentricity vs semi-major axis (colour graded according to eccentricity difference) clone 1")
plt.savefig("plots/Eccentricity_vs_semimajor_axis_E_colour_grade_clone1.svg")
plt.close()
