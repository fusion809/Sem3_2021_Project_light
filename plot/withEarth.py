#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import os
for astNo in range(1, 49):
    for clone in range(0, 9):
        df = pd.read_csv("../output/ordinary/output/coords_and_vel_" + str(astNo) + ".csv")
        t = df["t"]; x = df["x"]; y = df["y"]; z = df["z"]
        plt.plot(x[10000:20000], y[10000:20000], label="Earth")
        plt.plot(x[70000 + clone * 10000:80000 + clone * 10000], y[70000 + clone * 10000:80000 + clone * 10000], label="Asteroid " + str(astNo) + " clone " + str(clone))
        plt.legend()
        plt.title("Plot of asteroid " + str(astNo) + " clone " + str(clone) + " with the Earth")
        svgtitle = "../plots/withEarth/asteroid_" + str(astNo) + "_clone_" + str(clone) + ".svg"
        pngtitle = "../plots/withEarth/asteroid_" + str(astNo) + "_clone_" + str(clone) + ".png"
        plt.savefig(svgtitle)
        os.system("convert {} {}".format(svgtitle, pngtitle))
        plt.close()