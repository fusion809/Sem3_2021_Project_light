#!/usr/bin/env python
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

# DataFrame
Noutputs = 10000
for astNo in range(1, 49):
    df = pd.read_csv("coords_and_velBack_" + str(astNo) + ".csv")
    x = df["x"]
    y = df["y"]
    z = df["z"]
    xVenus = x[0:Noutputs]
    yVenus = y[0:Noutputs]
    xEarth = x[Noutputs:2*Noutputs]
    yEarth = y[Noutputs:2*Noutputs]
    xMars = x[2*Noutputs:3*Noutputs]
    yMars = y[2*Noutputs:3*Noutputs]
    xJupiter = x[3*Noutputs:4*Noutputs]
    yJupiter = y[3*Noutputs:4*Noutputs]
    for cloneNo in range(0, 9):
        xAst = x[(7 + cloneNo)*Noutputs:(8 + cloneNo)*Noutputs]
        yAst = y[(7 + cloneNo)*Noutputs:(8 + cloneNo)*Noutputs]
        plt.figure(1, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xMars, yMars, label="Mars")
        plt.plot(xAst, yAst, label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        title="Asteroid " + str(astNo) + " clone " + str(cloneNo) + " back simulation 10 My using IAS15"
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        svgfile = "../../plots/backIAS151e7/VEMA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = "../../plots/backIAS151e7/VEMA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()
    
        plt.figure(2, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xAst, yAst, label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        svgfile = "../../plots/backIAS151e7/VEA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = "../../plots/backIAS151e7/VEA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()

        plt.figure(3, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xAst, yAst, label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        svgfile = "../../plots/backIAS151e7/VA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = "../../plots/backIAS151e7/VA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()

        plt.figure(4, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xMars, yMars, label="Mars")
        plt.plot(xJupiter, yJupiter, label="Jupiter")
        plt.plot(xAst, yAst, label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        svgfile = "../../plots/backIAS151e7/VEMJA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = "../../plots/backIAS151e7/VEMJA_asteroid_" + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()
