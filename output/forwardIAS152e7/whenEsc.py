#!/usr/bin/env python
import pandas as pd
import numpy as np
import argparse

# Args
title = 'Plot the trajectory of celestial bodies in specified file'
parser = argparse.ArgumentParser(description=title)
parser.add_argument('integer', metavar='no', type=int, nargs="+", 
help="Integers specifying the file to be used")
args = parser.parse_args()
no = args.integer[0]

# Import coordinates
df = pd.read_csv("coords_and_vel_" + str(no) + ".csv")
x = np.array(df["x"])
y = np.array(df["y"])
z = np.array(df["z"])
t = np.array(df["t"])

# Determine distance from Solar system barycentre
d = np.sqrt(np.power(x, 2) + np.power(y, 2) + np.power(z, 2))

# Find the times at which each object escapes the Solar system (d > 100)
Noutputs = 10000
ind = [i for i in range(0, 16*Noutputs)]
ind = np.array(ind)
indices = ind[d > 100]
escInd = np.array([])
for i in range(0, 16):
    indR = indices[i*Noutputs <= indices]
    indR = indR[indR < (i+1)*Noutputs]
    escInd = np.append(escInd, int(np.min(indR)))
escInd = escInd.astype(int)
escTimes = t[escInd]

# Print escape times in user-friendly way
objects = ["Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
counter = 0
for time in escTimes:
    if (counter < 7):
        planStr = "Escape time for %s = %0.2f million years in the future"
        print(planStr%(objects[counter], escTimes[counter]/1e6))
    else:
        astStr = "Escape time for asteroid %d clone %d = %0.2f million years "
        astStr += "in the future"
        print(astStr%(no, counter - 7, escTimes[counter]/1e6))
    counter += 1
