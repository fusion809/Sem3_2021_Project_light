#!/usr/bin/env python
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import pandas as pd
import os

Noutputs = 10000

# Plot each clone relative to the terrestrial planets we've modelled
for no in range(1, 49):
    # Read data
    basedir = "../output/ordinary/output/"
    file = basedir + "coords_and_vel_" + str(no) + ".csv"
    paramsFile = basedir + "parameters_" + str(no) + ".csv"
    df = pd.read_csv(file, sep=",")
    paramsDf = pd.read_csv(paramsFile, sep=",")
    times = df['t']
    x = df['x']
    y = df['y']
    z = df['z']
    a = paramsDf['a']
    e = paramsDf['e']
    inc = paramsDf['inc']

    for i in range(0, 9):
        # Starting index 
        startIndex = (i + 7) * Noutputs
        endIndex = (i + 8) * Noutputs
        asteroidLabel = "Asteroid_" + str(no) + "_clone_" + str(i)
        asteroidLabelTeX = "Asteroid " + str(no) + " clone " + str(i)

        # First figure is a plot of the ith clone of the asteroid and 
        # Venus, Earth and Mars
        plt.figure(1, figsize=(8,6))
        plt.plot(x[0:Noutputs], y[0:Noutputs], label="Venus")
        plt.plot(x[Noutputs:2*Noutputs], y[Noutputs:2*Noutputs], 
        label="Earth")
        plt.plot(x[2*Noutputs:3*Noutputs], y[2*Noutputs:3*Noutputs], 
        label="Mars", alpha=0.6)
        plt.plot(x[3*Noutputs:4*Noutputs], y[3*Noutputs:4*Noutputs], 
        label="Jupiter")
        plt.plot(x[startIndex:endIndex], y[startIndex:endIndex], 
        label=asteroidLabelTeX, color="#c85200")
        plt.scatter(0, 0, label="Sun", color="black")
        plt.xlabel(r"$x$ (au)", fontsize=18)
        plt.xticks(fontsize=16)
        plt.xlim([-5.6, 5.6])
        plt.ylim([-5.6, 5.6])
        plt.tight_layout(rect=[0.035, 0, 0.654, 0.9])
        plt.ylabel(r"$y$ (au)", fontsize=18)
        plt.yticks(fontsize=16)
        Ptitle = "Trajectory of Venus, Earth, Mars, Jupiter\n and " 
        Ptitle += asteroidLabelTeX
        plt.title(Ptitle, fontsize=20)
        plt.legend(bbox_to_anchor=(1.69, 1.05), ncol=1, loc="upper right", 
        fontsize=18)
        PDir = "../plots/N1e8Noutputs1e4/"
        svgtitle1 = PDir + asteroidLabel + "_wo_Jupiter_et_al.svg"
        pngtitle1 = PDir + asteroidLabel + "_wo_Jupiter_et_al.png"
        plt.savefig(svgtitle1)
        os.system("convert {} {}".format(svgtitle1, pngtitle1))
        plt.close(fig=1)

        # Semi-major axis vs time plot
        plt.figure(2, figsize=(8, 6))
        plt.plot(times[startIndex:endIndex], a[startIndex:endIndex], 
        label=asteroidLabelTeX)
        plt.xlabel(r"$t$ (years)", fontsize=18)
        plt.xticks(fontsize=16)
        plt.ylabel("Semi-major axis (au)", fontsize=18)
        plt.yticks(fontsize=16)
        plt.title("Semi-major axis vs time plot for " + asteroidLabelTeX, 
        fontsize=20)
        plt.legend(fontsize=18)
        SMADir = "../plots/Semimajor_axis/"
        svgtitle2 = SMADir + asteroidLabel + "_semimajor_time.svg"
        pngtitle2 = SMADir + asteroidLabel + "_semimajor_time.png"
        plt.savefig(svgtitle2)
        os.system("convert {} {}".format(svgtitle2, pngtitle2))
        plt.close(fig=2)

        # Eccentricity vs time plot
        plt.figure(3)
        plt.plot(times[startIndex:endIndex], e[startIndex:endIndex], 
        label=asteroidLabelTeX)
        plt.xlabel(r"$t$ (years)", fontsize=18)
        plt.xticks(fontsize=16)
        plt.ylabel("Eccentricity", fontsize=18)
        plt.yticks(fontsize=16)
        plt.title("Eccentricity vs time plot for " + asteroidLabelTeX, 
        fontsize=20)
        plt.legend(fontsize=18)
        EDir = "../plots/Eccentricity/"
        svgtitle3 = EDir + asteroidLabel + "_eccentricity_time.svg"
        pngtitle3 = EDir + asteroidLabel + "_eccentricity_time.png"
        plt.savefig(svgtitle3)
        os.system("convert {} {}".format(svgtitle3, pngtitle3))
        plt.close(fig=3)
        
        # Inclination vs time plot
        plt.figure(4)
        plt.plot(times[startIndex:endIndex], inc[startIndex:endIndex], 
        label=asteroidLabelTeX)
        plt.xlabel(r"$t$ (years)", fontsize=18)
        plt.xticks(fontsize=16)
        plt.ylabel("Inclination", fontsize=18)
        plt.yticks(fontsize=16)
        plt.title("Inclination vs time plot for " + asteroidLabelTeX, 
        fontsize=20)
        plt.legend(fontsize=18)
        IDir = "../plots/Inclination/"
        svgtitle4 = IDir + asteroidLabel + "_inclination_time.svg"
        pngtitle4 = IDir + asteroidLabel + "_inclination_time.png"
        plt.savefig(svgtitle4)
        os.system("convert {} {}".format(svgtitle4, pngtitle4))
        plt.close(fig=4)
