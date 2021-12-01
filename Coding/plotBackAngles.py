#!/usr/bin/env python
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import numpy as np
import pandas as pd

Noutputs = 10000
Nmax = Noutputs
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
    df = pd.read_csv("output/back/coords_and_velBack_" + str(i) + ".csv")
    dfParam = pd.read_csv("output/back/parametersBack_" + str(i) + ".csv")
    t = df['t']
    Omega = dfParam['Omega']
    f = dfParam['f']
    nodalLong = Omega
    plt.plot(t[0:Nmax], nodalLong[70000:70000 + Nmax] * 180/np.pi)
    # plt.plot(t[0:Noutputs], nodalLong[80000:90000])
    # plt.plot(t[0:Noutputs], nodalLong[90000:100000])
    # plt.plot(t[0:Noutputs], nodalLong[100000:110000])
    # plt.plot(t[0:Noutputs], nodalLong[110000:120000])
    # plt.plot(t[0:Noutputs], nodalLong[120000:130000])
    # plt.plot(t[0:Noutputs], nodalLong[130000:140000])
    # plt.plot(t[0:Noutputs], nodalLong[140000:150000])
    # plt.plot(t[0:Noutputs], nodalLong[150000:160000])
plt.xlabel("t (years)")
plt.ylabel("Nodal longitude (degrees)")
plt.title("Nodal longitude against time")
plt.savefig("plots/Nodal_longitude_plot.svg")
plt.figure(2)
for i in range(1, astMax):
    df = pd.read_csv("output/back/coords_and_velBack_" + str(i) + ".csv")
    dfParam = pd.read_csv("output/back/parametersBack_" + str(i) + ".csv")
    t = df['t']
    Omega = dfParam['Omega']
    omega = dfParam['omega']
    f = dfParam['f']
    periLong = omega
    plt.plot(t[0:Nmax], periLong[70000:70000 + Nmax] * 180/np.pi)
    # plt.plot(t[0:Noutputs], periLong[80000:90000])
    # plt.plot(t[0:Noutputs], periLong[90000:100000])
    # plt.plot(t[0:Noutputs], periLong[100000:110000])
    # plt.plot(t[0:Noutputs], periLong[110000:120000])
    # plt.plot(t[0:Noutputs], periLong[120000:130000])
    # plt.plot(t[0:Noutputs], periLong[130000:140000])
    # plt.plot(t[0:Noutputs], periLong[140000:150000])
    # plt.plot(t[0:Noutputs], periLong[150000:160000])
plt.xlabel("t (years)")
plt.ylabel("Perihelion longitude (degrees)")
plt.title("Perihelion longitude against time")
plt.savefig("plots/Perihelion_longitude_plot.svg")
# 3-5 Hill radii, if it crosses that start the simulation at the 
# time step - 1 until it leaves the 3-5 Hill radii.
# If any object is NEA, add to simulation with Bennu
# Start characterizing asteroids by whether they get ejected, become centaurs 
# or neos.
# Maybe make graphs colourblind friendly.