#!/usr/bin/env python
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import numpy as np
import pandas as pd
import os

Noutputs = 10000
# 0 - 9999 Venus
# 10000 - 19999 Earth
# 20000 - 29999 Mars
# 30000 - 39999 Jupiter
# 40000 - 49999 Saturn
# 50000 - 59999 Uranus
# 60000 - 69999 Neptune
# 70000 - 16000 Asteroids clones 0 to 9
plt.figure(1)
astMax = 48
astMax += 1
for i in range(1, astMax):
    df = pd.read_csv("../output/backIAS151e7/coords_and_velBack_" + str(i) + ".csv")
    dfParam = pd.read_csv("../output/backIAS151e7/parametersBack_" + str(i) + ".csv")
    t = df['t']
    Omega = dfParam['Omega']
    plt.plot(t[0:Noutputs], Omega[70000:70000 + Noutputs] * 180/np.pi)
plt.xlabel("t (years)")
plt.ylabel("Nodal longitude (degrees)")
plt.title("Nodal longitude against time")
svgtitle1 = "../plots/Angles/Nodal_longitude_plot.svg"
pngtitle1 = "../plots/Angles/Nodal_longitude_plot.png"
plt.savefig()
os.system("convert {} {}".format(svgtitle1, pngtitle1))
plt.figure(2)
for i in range(1, astMax):
    df = pd.read_csv("../output/backIAS151e7/coords_and_velBack_" + str(i) + ".csv")
    dfParam = pd.read_csv("../output/backIAS151e7/parametersBack_" + str(i) + ".csv")
    t = df['t']
    omega = dfParam['omega']
    plt.plot(t[0:Noutputs], omega[70000:70000 + Noutputs] * 180/np.pi)
plt.xlabel("t (years)")
plt.ylabel("Perihelion longitude (degrees)")
plt.title("Perihelion longitude against time")
svgtitle2 = "../plots/Angles/Perihelion_longitude_plot.svg"
pngtitle2 = "../plots/Angles/Perihelion_longitude_plot.png"
plt.savefig(svgtitle2)
os.system("convert {} {}".format(svgtitle2, pngtitle2))