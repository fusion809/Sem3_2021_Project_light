#!/usr/bin/env python
import os
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import pandas as pd


for no in range(1, 49):
    # Read file
    file = "../output/back/coords_and_velBack_" + str(no) + ".csv"
    paramsFile = "../output/back/parametersBack_" + str(no) + ".csv"
    df = pd.read_csv(file, sep=",")
    paramsDf = pd.read_csv(paramsFile, sep=",")
    times = df['t']
    x = df['x']
    y = df['y']
    z = df['z']
    a = paramsDf['a']
    e = paramsDf['e']
    inc = paramsDf['inc']
    Noutputs = 10000

    # Plot each clone relative to the terrestrial planets we've modelled
    for i in range(0, 9):
        # Starting index 
        startIndex = (i + 7) * Noutputs
        endIndex = (i + 8) * Noutputs
        asteroidLabel = "Asteroid_" + str(no) + "_clone_" + str(i)
        asteroidLabelTeX = "Asteroid " + str(no) + " clone " + str(i)

        # First figure is a plot of the ith clone of the asteroid and 
        # Venus, Earth and Mars
        plt.figure(1)
        plt.plot(x[0:Noutputs], y[0:Noutputs], label="Venus")
        plt.plot(x[Noutputs:2*Noutputs], y[Noutputs:2*Noutputs], label="Earth")
        plt.plot(x[2*Noutputs:3*Noutputs], y[2*Noutputs:3*Noutputs], label="Mars")
        plt.plot(x[3*Noutputs:4*Noutputs], y[3*Noutputs:4*Noutputs], label="Jupiter")
        plt.plot(x[startIndex:endIndex], y[startIndex:endIndex], label=asteroidLabelTeX)
        plt.xlabel("x (AU)")
        plt.ylabel("y (AU)")
        plt.title("Trajectory of Venus, Earth, Mars, Jupiter and " + asteroidLabelTeX)
        plt.legend()
        svgtitle1 = "../plots/N1e8Noutputs1e4/" + asteroidLabel + "_back_wo_Jupiter_et_al.svg"
        pngtitle1 = "../plots/N1e8Noutputs1e4/" + asteroidLabel + "_back_wo_Jupiter_et_al.png"
        plt.savefig(svgtitle1)
        os.system("convert {} {}".format(svgtitle1, pngtitle1))
        plt.close(fig=1)

        # Semi-major axis vs time plot
        plt.figure(2)
        plt.plot(times[startIndex:endIndex], a[startIndex:endIndex], label=asteroidLabelTeX)
        plt.xlabel("t (years)")
        plt.ylabel("Semimajor axis (AU)")
        plt.title("Semimajor axis vs time plot for " + asteroidLabelTeX)
        plt.legend()
        svgtitle2 = "../plots/Semimajor_axis/" + asteroidLabel + "_back_semimajor_time.svg"
        pngtitle2 = "../plots/Semimajor_axis/" + asteroidLabel + "_back_semimajor_time.png"
        plt.savefig(svgtitle2)
        os.system("convert {} {}".format(svgtitle2, pngtitle2))
        plt.close(fig=2)

        # Eccentricity vs time plot
        plt.figure(3)
        plt.plot(times[startIndex:endIndex], e[startIndex:endIndex], label=asteroidLabelTeX)
        plt.xlabel("t (years)")
        plt.ylabel("Eccentricity")
        plt.title("Eccentricity vs time plot for " + asteroidLabelTeX)
        plt.legend()
        svgtitle3 = "../plots/Eccentricity/" + asteroidLabel + "_back_eccentricity_time.svg"
        pngtitle3 = "../plots/Eccentricity/" + asteroidLabel + "_back_eccentricity_time.png"
        plt.savefig(svgtitle3)
        os.system("convert {} {}".format(svgtitle3, pngtitle3))
        plt.close(fig=3)
        
        # Inclination vs time plot
        plt.figure(4)
        plt.plot(times[startIndex:endIndex], inc[startIndex:endIndex], label=asteroidLabelTeX)
        plt.xlabel("t (years)")
        plt.ylabel("Inclination")
        plt.title("Inclination vs time plot for " + asteroidLabelTeX)
        plt.legend()
        svgtitle4 = "../plots/Inclination/" + asteroidLabel + "_back_inclination_time.svg"
        pngtitle4 = "../plots/Inclination/" + asteroidLabel + "_back_inclination_time.png"
        plt.savefig(svgtitle4)
        os.system("convert {} {}".format(svgtitle4, pngtitle4))
        plt.close(fig=4)
