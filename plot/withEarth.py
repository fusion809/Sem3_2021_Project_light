#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import os
Noutputs = 10000

# Plot Earth and asteroid clone 0 on same plot
for astNo in range(1, 49):
    for clone in range(0, 9):
        coordsVelBase = "../output/ordinary/output/coords_and_vel_"
        df = pd.read_csv(coordsVelBase + str(astNo) + ".csv")
        t = df["t"]
        x = df["x"]
        y = df["y"]
        plt.plot(x[Noutputs:2*Noutputs], y[Noutputs:2*Noutputs], 
        label="Earth")
        astSt = (7 + clone) * Noutputs
        astEnd = (8 + clone) * Noutputs
        plt.plot(x[astSt:astEnd], y[astSt:astEnd], 
        label="Asteroid " + str(astNo) + " clone " + str(clone))
        plt.legend()
        title = "Plot of asteroid " + str(astNo) + " clone " + str(clone)
        title += " with the Earth"
        plt.title(title)
        pltBase = "../plots/withEarth/asteroid_"
        svgtitle = pltBase + str(astNo) + "_clone_" + str(clone) + ".svg"
        pngtitle = pltBase + str(astNo) + "_clone_" + str(clone) + ".png"
        plt.savefig(svgtitle)
        os.system("convert {} {}".format(svgtitle, pngtitle))
        plt.close()