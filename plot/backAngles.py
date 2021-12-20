#!/usr/bin/env python
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import numpy as np
import pandas as pd

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
    # plt.plot(t[0:Noutputs], Omega[80000:90000])
    # plt.plot(t[0:Noutputs], Omega[90000:100000])
    # plt.plot(t[0:Noutputs], Omega[100000:110000])
    # plt.plot(t[0:Noutputs], Omega[110000:120000])
    # plt.plot(t[0:Noutputs], Omega[120000:130000])
    # plt.plot(t[0:Noutputs], Omega[130000:140000])
    # plt.plot(t[0:Noutputs], Omega[140000:150000])
    # plt.plot(t[0:Noutputs], Omega[150000:160000])
plt.xlabel("t (years)")
plt.ylabel("Nodal longitude (degrees)")
plt.title("Nodal longitude against time")
plt.savefig("../plots/Angles/Nodal_longitude_plot.svg")
plt.figure(2)
for i in range(1, astMax):
    df = pd.read_csv("../output/backIAS151e7/coords_and_velBack_" + str(i) + ".csv")
    dfParam = pd.read_csv("../output/backIAS151e7/parametersBack_" + str(i) + ".csv")
    t = df['t']
    omega = dfParam['omega']
    plt.plot(t[0:Noutputs], omega[70000:70000 + Noutputs] * 180/np.pi)
    # plt.plot(t[0:Noutputs], omega[80000:90000])
    # plt.plot(t[0:Noutputs], omega[90000:100000])
    # plt.plot(t[0:Noutputs], omega[100000:110000])
    # plt.plot(t[0:Noutputs], omega[110000:120000])
    # plt.plot(t[0:Noutputs], omega[120000:130000])
    # plt.plot(t[0:Noutputs], omega[130000:140000])
    # plt.plot(t[0:Noutputs], omega[140000:150000])
    # plt.plot(t[0:Noutputs], omega[150000:160000])
plt.xlabel("t (years)")
plt.ylabel("Perihelion longitude (degrees)")
plt.title("Perihelion longitude against time")
plt.savefig("../plots/Angles/Perihelion_longitude_plot.svg")
# 3-5 Hill radii, if it crosses that start the simulation at the 
# time step - 1 until it leaves the 3-5 Hill radii.
# If any object is NEA, add to simulation with Bennu
# Start characterizing asteroids by whether they get ejected, become centaurs 
# or neos.
# Maybe make graphs colourblind friendly.
